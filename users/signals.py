from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.utils.timezone import now
from .models import UserProfile


def user_logged(sender, request, user, **kwargs):
    if not user.is_superuser:
        profile, created = UserProfile.objects.get_or_create(user=user)
        profile.login_time = now()
        profile.save()


def user_logout(sender, request, user, **kwargs):
    if not user.is_superuser:
        profile, created = UserProfile.objects.get_or_create(user=user)
        profile.logout_time = now()
        profile.total_session_time = profile.logout_time - profile.login_time
        profile.save()


user_logged_in.connect(user_logged)
user_logged_out.connect(user_logout)
