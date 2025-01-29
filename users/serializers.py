from rest_framework import serializers
from .models import UserProfile, LandingPage


class UserProfileSerializer(serializers.ModelSerializer):
    login_time = serializers.DateTimeField(
        format="%Y/%m/%d %H:%M:%S", required=False, allow_null=True)
    logout_time = serializers.DateTimeField(
        format="%Y/%m/%d %H:%M:%S", required=False, allow_null=True)
    session_duration = serializers.SerializerMethodField()

    class Meta:
        model = UserProfile
        fields = ['user', 'login_time', 'logout_time',
                  'session_duration', 'button1_clicks', 'button2_clicks']

    def get_session_duration(self, obj):
        if obj.logout_time and obj.login_time:
            total_seconds = int(obj.total_session_time.total_seconds(
            )) if obj.total_session_time is not None else 0
            hours = total_seconds // 3600
            minutes = (total_seconds % 3600) // 60
            seconds = total_seconds % 60
            return f"{hours:02}:{minutes:02}:{seconds:02}"
        return "00:00:00"


class LandingPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = LandingPage
        fields = "__all__"
