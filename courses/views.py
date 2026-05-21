from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from .models import Lesson
from progress.models import UserLessonProgress


@login_required
def lesson_list(request):
    lessons = list(Lesson.objects.filter(is_published=True).order_by("order"))
    progress_map = {p.lesson_id: p for p in UserLessonProgress.objects.filter(user=request.user)}
    rows = []
    for i, lesson in enumerate(lessons):
        unlocked = True
        if i > 0:
            prev_progress = progress_map.get(lessons[i - 1].id)
            unlocked = bool(prev_progress and prev_progress.is_completed)
        rows.append({
            "lesson": lesson,
            "unlocked": unlocked,
            "progress": progress_map.get(lesson.id),
        })
    return render(request, "courses/lesson_list.html", {"lesson_rows": rows})


@login_required
def lesson_detail(request, slug):
    lesson = get_object_or_404(Lesson, slug=slug, is_published=True)
    if not lesson.is_unlocked_for(request.user):
        messages.error(request, "Complete the previous lesson first.")
        return redirect("lesson_list")

    progress = UserLessonProgress.objects.filter(user=request.user, lesson=lesson).first()

    prev_lesson = (
        Lesson.objects.filter(order__lt=lesson.order, is_published=True)
        .order_by("-order")
        .first()
    )
    next_lesson = (
        Lesson.objects.filter(order__gt=lesson.order, is_published=True)
        .order_by("order")
        .first()
    )

    return render(request, "courses/lesson_detail.html", {
        "lesson": lesson,
        "progress": progress,
        "prev_lesson": prev_lesson,
        "next_lesson": next_lesson,
    })
