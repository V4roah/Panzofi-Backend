import os
import django
from datetime import datetime
from django.contrib.auth.models import User
from users.models import UserProfile

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
django.setup()

for i in range(1, 36):
    username = f'user_{i}'
    email = f'user{i}@example.com'
    password = 'password123'

    user = User.objects.create_user(
        username=username, email=email, password=password)

    profile = UserProfile.objects.create(
        user=user,
        login_time=datetime.now(),
        logout_time=datetime.now(),
        button1_clicks=0,
        button2_clicks=0,
        total_session_time="00:00:00"
    )

    print(f"Usuario {username} creado exitosamente.")
