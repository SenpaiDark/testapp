from django.contrib import admin
from .models import Certificate, UserLessonProgress

@admin.register(UserLessonProgress)
class UserLessonProgressAdmin(admin.ModelAdmin):
    list_display = ("user", "lesson", "score", "is_completed", "updated_at")
    list_filter = ("is_completed",)

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ("user", "certificate_code", "issued_at", "total_lessons", "avg_score")
    search_fields = ("user__username", "certificate_code")
