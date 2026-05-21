from django.urls import path
from . import views

urlpatterns = [
    path("<slug:lesson_slug>/", views.take_quiz, name="take_quiz"),
]
