from django.contrib.auth.models import User
from django.db import models
from courses.models import Lesson

class UserLessonProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="lesson_progress")
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name="user_progress")
    score = models.PositiveIntegerField(default=0)
    is_completed = models.BooleanField(default=False)
    attempts = models.PositiveIntegerField(default=0)
    completed_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("user", "lesson")
        ordering = ["lesson__order"]

    def __str__(self):
        return f"{self.user.username} - {self.lesson.title} - {self.score}%"
