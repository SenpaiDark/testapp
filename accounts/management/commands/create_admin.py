from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from decouple import config


class Command(BaseCommand):
    help = "Create a superuser from env vars if none exists"

    def handle(self, *args, **kwargs):
        username = config("ADMIN_USERNAME", default="admin")
        password = config("ADMIN_PASSWORD", default="")
        email = config("ADMIN_EMAIL", default="admin@mayor4code.com")

        if not password:
            self.stdout.write("ADMIN_PASSWORD not set — skipping superuser creation.")
            return

        if User.objects.filter(is_superuser=True).exists():
            self.stdout.write("Superuser already exists — skipping.")
            return

        User.objects.create_superuser(username=username, email=email, password=password)
        self.stdout.write(f"Superuser '{username}' created.")
