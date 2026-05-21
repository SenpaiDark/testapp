from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST
from django.db.models import Avg, Sum, Count, Q
from courses.models import Lesson
from progress.models import UserLessonProgress
from .forms import RegisterForm


def home(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    return render(request, "accounts/home.html")


def register_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    form = RegisterForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.save()
        login(request, user)
        return redirect("dashboard")
    return render(request, "accounts/register.html", {"form": form})


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

    return render(request, "accounts/dashboard.html", {
        "lesson_rows": lesson_rows,
        "total_count": total_count,
        "completed_count": completed_count,
        "progress_pct": progress_pct,
    })


@login_required
def profile_view(request):
    lessons = list(Lesson.objects.filter(is_published=True).order_by("order"))
    all_progress = UserLessonProgress.objects.filter(user=request.user)
    progress_map = {p.lesson_id: p for p in all_progress}

    completed_count = sum(1 for p in all_progress if p.is_completed)
    total_count = len(lessons)
    progress_pct = round((completed_count / total_count) * 100) if total_count else 0

    agg = all_progress.aggregate(avg=Avg("score"), total_attempts=Sum("attempts"))
    avg_score = round(agg["avg"]) if agg["avg"] else None
    total_attempts = agg["total_attempts"] or 0

    return render(request, "accounts/profile.html", {
        "profile_user": request.user,
        "completed_count": completed_count,
        "total_count": total_count,
        "progress_pct": progress_pct,
        "avg_score": avg_score,
        "total_attempts": total_attempts,
    })


@login_required
def leaderboard_view(request):
    total_lessons = Lesson.objects.filter(is_published=True).count()

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
