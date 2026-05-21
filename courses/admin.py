from django.contrib import admin
from .models import Lesson

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("order", "title", "is_published")
    prepopulated_fields = {"slug": ("title",)}
    ordering = ("order",)
