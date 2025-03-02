from django.core.management.base import BaseCommand
from user.models import User
from django.contrib.auth.hashers import make_password

class Command(BaseCommand):
    help = 'Seed the database with initial data'

    def handle(self, *args, **kwargs):
        try:
            users_data = [
                {
                    'username': 'john_doe',
                    'email': 'john_doe@example.com',
                    'password': make_password('password123'),
                    'role': 'owner'
                },
                {
                    'username': 'jane_smith',
                    'email': 'jane_smith@example.com',
                    'password': make_password('password123'),
                    'role': 'user'
                }
            ]

            for user_data in users_data:
                user, created = User.objects.get_or_create(email=user_data['email'], defaults=user_data)
                if created:
                    self.stdout.write(self.style.SUCCESS(f"User {user.username} created successfully"))
                else:
                    self.stdout.write(self.style.WARNING(f"User {user.username} already exists"))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error seeding data: {str(e)}"))
