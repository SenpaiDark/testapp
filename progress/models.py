from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now
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


class Certificate(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="certificate")
    issued_at = models.DateTimeField(default=now)
    certificate_code = models.CharField(max_length=20, unique=True, blank=True)
    total_lessons = models.PositiveIntegerField(default=5)
    avg_score = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["-issued_at"]

    def save(self, *args, **kwargs):
        if not self.certificate_code:
            import secrets
            code = secrets.token_hex(4).upper()
            self.certificate_code = f"CERT-{code}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Certificate for {self.user.username} — {self.certificate_code}"
