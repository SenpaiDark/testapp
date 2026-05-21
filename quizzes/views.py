from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from courses.models import Lesson
from progress.models import UserLessonProgress
from .models import Quiz

@login_required
def take_quiz(request, lesson_slug):
    lesson = get_object_or_404(Lesson, slug=lesson_slug, is_published=True)
    quiz = get_object_or_404(Quiz, lesson=lesson)
    questions = quiz.questions.all()

    results = None
    percent = None
    completed = None

    if request.method == "POST":
        total = questions.count()
        if total == 0:
            messages.error(request, "No questions have been added for this quiz yet.")
            return redirect("lesson_detail", slug=lesson.slug)

        score_count = 0
        question_results = []
        for question in questions:
            selected = request.POST.get(f"question_{question.id}")
            is_correct = selected == question.correct_option
            if is_correct:
                score_count += 1
            question_results.append({
                "question": question,
                "selected": selected or "",
                "correct": question.correct_option,
                "is_correct": is_correct,
            })

        percent = round((score_count / total) * 100)
        completed = percent >= quiz.pass_mark

        progress, created = UserLessonProgress.objects.get_or_create(
            user=request.user,
            lesson=lesson,
        )
        progress.score = percent
        progress.is_completed = completed
        progress.attempts += 1
        if completed and not progress.completed_at:
            progress.completed_at = timezone.now()
        progress.save()

        results = {
            "score_count": score_count,
            "total": total,
            "percent": percent,
            "completed": completed,
            "questions": question_results,
            "pass_mark": quiz.pass_mark,
        }

    return render(request, "quizzes/quiz.html", {
        "quiz": quiz,
        "lesson": lesson,
        "questions": questions,
        "results": results,
    })
