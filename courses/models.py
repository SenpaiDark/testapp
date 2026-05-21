from django.db import models
from django.utils.text import slugify

class Lesson(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    order = models.PositiveIntegerField(unique=True)
    summary = models.CharField(max_length=255, blank=True)
    content = models.TextField(help_text="You can paste lesson content here.")
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["order"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def is_unlocked_for(self, user):
        from progress.models import UserLessonProgress
        previous = (
            Lesson.objects.filter(order__lt=self.order, is_published=True)
            .order_by("-order")
            .first()
        )
        if not previous:
            return True
        prog = UserLessonProgress.objects.filter(user=user, lesson=previous).first()
        return bool(prog and prog.is_completed)

    def __str__(self):
        return f"{self.order}. {self.title}"
