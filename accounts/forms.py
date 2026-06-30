from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    matric_number = forms.CharField(
        max_length=20,
        required=True,
        label="Matric Number",
        widget=forms.TextInput(attrs={"placeholder": "e.g. CSC/2021/001"}),
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def save(self, commit=True):
        user = super().save(commit=commit)
        if commit:
            from .models import UserProfile
            profile, _ = UserProfile.objects.get_or_create(user=user)
            profile.matric_number = self.cleaned_data["matric_number"]
            profile.save()
        return user
