from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    login_time = models.DateTimeField(null=True, blank=True)
    logout_time = models.DateTimeField(null=True, blank=True)
    button1_clicks = models.IntegerField(default=0)
    button2_clicks = models.IntegerField(default=0)
    total_session_time = models.DurationField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.login_time and self.logout_time:
            duration = self.logout_time - self.login_time
            if duration.total_seconds() > 0:
                self.total_session_time = duration
            else:
                self.total_session_time = timedelta(
                    seconds=0)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.user.username


class LandingPage(models.Model):
    logo = models.ImageField(upload_to='logos/')
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title
