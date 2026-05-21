from django.contrib import admin
from .models import UserLessonProgress

@admin.register(UserLessonProgress)
class UserLessonProgressAdmin(admin.ModelAdmin):
    list_display = ("user", "lesson", "score", "is_completed", "updated_at")
    list_filter = ("is_completed",)
