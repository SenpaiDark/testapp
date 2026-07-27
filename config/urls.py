from django.contrib import admin
from django.urls import include, path
from accounts.views import admin_gate, admin_logout
from config.pwa_views import service_worker, manifest

urlpatterns = [
    path("panel/", admin.site.urls),       # real Django admin — gate-protected
    path("admin/", admin_gate),            # custom gate login
    path("admin/logout/", admin_logout),   # gate logout
    path("sw.js", service_worker),
    path("manifest.json", manifest),
    path("", include("accounts.urls")),
    path("lessons/", include("courses.urls")),
    path("quizzes/", include("quizzes.urls")),
]
