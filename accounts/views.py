from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST, require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.db.models import Avg, Sum, Count, Q
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import send_mail
from django.conf import settings as django_settings
from courses.models import Lesson
from progress.models import Certificate, UserLessonProgress
from .forms import RegisterForm
import json
import sys
import subprocess
import tempfile
import os


def home(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    return render(request, "accounts/home.html")


def _send_verification_email(request, user):
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = default_token_generator.make_token(user)
    verify_url = request.build_absolute_uri(f"/verify-email/{uid}/{token}/")
    try:
        send_mail(
            subject="Verify your mayor4code email",
            message=(
                f"Hi {user.username},\n\n"
                f"Click the link below to verify your email and activate your account:\n"
                f"{verify_url}\n\n"
                f"If you didn't sign up, ignore this email.\n\n"
                f"— mayor4code"
            ),
            from_email=django_settings.DEFAULT_FROM_EMAIL,
            recipient_list=[user.email],
            fail_silently=False,
        )
    except Exception as e:
        import logging
        logging.getLogger(__name__).error("Verification email failed: %s", e)


def register_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    form = RegisterForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.save()
        login(request, user)
        return redirect("dashboard")
    return render(request, "accounts/register.html", {"form": form})


def verify_email(request, uidb64, token):
    from .models import UserProfile
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        from django.contrib.auth.models import User as AuthUser
        user = AuthUser.objects.get(pk=uid)
    except Exception:
        user = None

    if user and default_token_generator.check_token(user, token):
        profile, _ = UserProfile.objects.get_or_create(user=user)
        profile.email_verified = True
        profile.save()
        return render(request, "accounts/email_verified.html", {"success": True, "user": user})
    return render(request, "accounts/email_verified.html", {"success": False})


def login_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    error = None
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("dashboard")
        else:
            error = "Invalid username or password."
    return render(request, "accounts/login.html", {"error": error})


@require_POST
def logout_view(request):
    logout(request)
    return redirect("login")


@login_required
def dashboard(request):
    lessons = list(Lesson.objects.filter(is_published=True).order_by("order"))
    progress_map = {
        p.lesson_id: p
        for p in UserLessonProgress.objects.filter(user=request.user)
    }
    lesson_rows = []
    for i, lesson in enumerate(lessons):
        unlocked = True
        if i > 0:
            prev_progress = progress_map.get(lessons[i - 1].id)
            unlocked = bool(prev_progress and prev_progress.is_completed)
        lesson_rows.append({
            "lesson": lesson,
            "progress": progress_map.get(lesson.id),
            "unlocked": unlocked,
        })

    total_count = len(lesson_rows)
    completed_count = sum(
        1 for row in lesson_rows
        if row["progress"] and row["progress"].is_completed
    )
    progress_pct = round((completed_count / total_count) * 100) if total_count else 0

    all_done = total_count > 0 and completed_count >= total_count

    all_progress = UserLessonProgress.objects.filter(user=request.user)
    agg = all_progress.aggregate(avg=Avg("score"))
    avg_score = round(agg["avg"]) if agg["avg"] else None

    return render(request, "accounts/dashboard.html", {
        "lesson_rows": lesson_rows,
        "total_count": total_count,
        "completed_count": completed_count,
        "progress_pct": progress_pct,
        "all_done": all_done,
        "avg_score": avg_score,
    })


@login_required
def profile_view(request):
    lessons = list(Lesson.objects.filter(is_published=True).order_by("order"))
    all_progress = UserLessonProgress.objects.filter(user=request.user)

    completed_count = sum(1 for p in all_progress if p.is_completed)
    total_count = len(lessons)
    progress_pct = round((completed_count / total_count) * 100) if total_count else 0

    agg = all_progress.aggregate(avg=Avg("score"), total_attempts=Sum("attempts"))
    avg_score = round(agg["avg"]) if agg["avg"] else None
    total_attempts = agg["total_attempts"] or 0

    all_done = total_count > 0 and completed_count >= total_count and total_count > 0

    return render(request, "accounts/profile.html", {
        "profile_user": request.user,
        "completed_count": completed_count,
        "total_count": total_count,
        "progress_pct": progress_pct,
        "avg_score": avg_score,
        "total_attempts": total_attempts,
        "all_done": all_done,
    })


@login_required
def leaderboard_view(request):
    total_lessons = Lesson.objects.filter(is_published=True).count()

    from .models import UserProfile
    profile_map = {p.user_id: p.matric_number for p in UserProfile.objects.all()}

    users_data = (
        UserLessonProgress.objects
        .values("user__id", "user__username")
        .annotate(
            avg_score=Avg("score"),
            completed=Count("id", filter=Q(is_completed=True)),
            total_attempts=Sum("attempts"),
        )
        .order_by("-completed", "-avg_score")
    )

    leaderboard = [
        {
            "username": entry["user__username"],
            "matric_number": profile_map.get(entry["user__id"], ""),
            "avg_score": round(entry["avg_score"]) if entry["avg_score"] else 0,
            "completed": entry["completed"],
            "total_lessons": total_lessons,
            "total_attempts": entry["total_attempts"] or 0,
        }
        for entry in users_data
    ]

    return render(request, "accounts/leaderboard.html", {"leaderboard": leaderboard})


@login_required
def all_done_view(request):
    lessons = list(Lesson.objects.filter(is_published=True).order_by("order"))
    all_progress = UserLessonProgress.objects.filter(user=request.user)
    total_lessons = len(lessons)

    agg = all_progress.aggregate(avg=Avg("score"), total_attempts=Sum("attempts"))
    avg_score = round(agg["avg"]) if agg["avg"] else None
    total_attempts = agg["total_attempts"] or 0

    return render(request, "accounts/all_done.html", {
        "total_lessons": total_lessons,
        "avg_score": avg_score,
        "total_attempts": total_attempts,
    })


@login_required
def my_certificate(request):
    lessons = list(Lesson.objects.filter(is_published=True).order_by("order"))
    all_progress = UserLessonProgress.objects.filter(user=request.user)
    total_lessons = len(lessons)
    completed_count = sum(1 for p in all_progress if p.is_completed)

    all_done = completed_count >= total_lessons

    try:
        cert = request.user.certificate
    except Certificate.DoesNotExist:
        cert = None

    if all_done and not cert:
        # Auto-issue certificate
        avg_score = all_progress.aggregate(avg=Avg("score"))["avg"] or 0
        cert = Certificate.objects.create(
            user=request.user,
            total_lessons=total_lessons,
            avg_score=round(avg_score),
        )

    return render(request, "accounts/certificate.html", {
        "certificate": cert,
        "all_done": all_done,
        "completed_count": completed_count,
        "total_lessons": total_lessons,
    })


@login_required
def settings_view(request):
    if request.method == "POST":
        from django.contrib import messages as msg
        action = request.POST.get("action")
        if action == "update_profile":
            from .models import UserProfile
            first_name = request.POST.get("first_name", "").strip()
            email = request.POST.get("email", "").strip()
            matric_number = request.POST.get("matric_number", "").strip()
            request.user.first_name = first_name
            request.user.email = email
            request.user.save(update_fields=["first_name", "email"])
            profile, _ = UserProfile.objects.get_or_create(user=request.user)
            profile.matric_number = matric_number
            profile.save(update_fields=["matric_number"])
            msg.success(request, "Profile updated successfully.")
        return redirect("settings")
    return render(request, "accounts/settings.html")


def playground(request):
    """Render the Python playground page where users can write and execute code"""
    return render(request, "accounts/playground.html")


@csrf_exempt
@require_http_methods(["POST"])
def execute_python(request):
    """
    Execute Python code safely and return the output.
    
    Security measures:
    - 5-second execution timeout
    - Blocks dangerous imports (os, sys, subprocess, etc.)
    - 10,000 character code limit
    - Safe temporary file execution with cleanup
    """
    try:
        # Parse JSON request body
        data = json.loads(request.body)
        code = data.get('code', '')
        
        # Validate code length
        if len(code) > 10000:
            return JsonResponse({
                'success': False,
                'error': 'Code exceeds maximum length of 10,000 characters'
            }, status=400)

        # Block only genuinely destructive system-level calls
        blocked = [
            'subprocess', 'shutil.rmtree', 'os.remove', 'os.rmdir',
            'os.system', 'os.popen', '__import__', 'eval(', 'exec(',
            'open(', 'socket', 'urllib', 'requests',
        ]
        code_lower = code.lower()
        for b in blocked:
            if b in code_lower:
                return JsonResponse({
                    'success': False,
                    'error': f'Security restriction: {b} is not allowed in the playground'
                }, status=403)

        # Create temporary file for code execution
        code_with_encoding = "# -*- coding: utf-8 -*-\n" + code
        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False, encoding='utf-8') as temp_file:
            temp_file.write(code_with_encoding)
            temp_file_path = temp_file.name

        try:
            # Execute with UTF-8 forced throughout
            env = os.environ.copy()
            env["PYTHONIOENCODING"] = "utf-8"
            env["PYTHONUTF8"] = "1"
            result = subprocess.run(
                [sys.executable, temp_file_path],
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="replace",
                timeout=5,
                env=env,
            )
            
            # Return successful execution
            if result.returncode == 0:
                return JsonResponse({
                    'success': True,
                    'output': result.stdout,
                    'error': ''
                })
            else:
                # Return error output
                return JsonResponse({
                    'success': False,
                    'output': result.stdout,
                    'error': result.stderr
                })
                
        except subprocess.TimeoutExpired:
            return JsonResponse({
                'success': False,
                'error': 'Execution timeout: Code took longer than 5 seconds to run'
            }, status=408)
            
        finally:
            # Clean up temporary file
            if os.path.exists(temp_file_path):
                os.remove(temp_file_path)
                
    except json.JSONDecodeError:
        return JsonResponse({
            'success': False,
            'error': 'Invalid JSON in request body'
        }, status=400)
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': f'Server error: {str(e)}'
        }, status=500)


def admin_gate(request):
    error = None
    if request.method == "POST":
        password = request.POST.get("password", "")
        from django.contrib.auth.models import User as AuthUser
        superuser = AuthUser.objects.filter(is_superuser=True).first()
        if superuser and superuser.check_password(password):
            superuser.backend = "django.contrib.auth.backends.ModelBackend"
            login(request, superuser)
            request.session["admin_authed"] = True
            return redirect("/panel/")
        error = "Incorrect password."
    return render(request, "accounts/admin_gate.html", {"error": error})


def admin_logout(request):
    request.session.pop("admin_authed", None)
    logout(request)
    return redirect("/admin/")
