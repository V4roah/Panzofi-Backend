from rest_framework import viewsets
from .models import UserProfile, LandingPage
from .serializers import UserProfileSerializer, LandingPageSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    @action(detail=True, methods=['post'])
    def button_click(self, request, pk=None):
        user_profile = self.get_object()
        button = request.data.get('button')
        if button == 'button1':
            user_profile.button1_clicks += 1
        elif button == 'button2':
            user_profile.button2_clicks += 1
        user_profile.save()
        return Response({'message': 'Button clicked'})

    @action(detail=False, methods=['get'], permission_classes=[IsAdminUser])
    def analytics(self, request):
        profiles = UserProfile.objects.all()
        analytics_data = []
        for profile in profiles:
            data = {
                'username': profile.user.username,
                'login_time': profile.login_time,
                'logout_time': profile.logout_time,
                'session_duration': profile.total_session_time,
                'button1_clicks': profile.button1_clicks,
                'button2_clicks': profile.button2_clicks,
            }
            analytics_data.append(data)
        return Response(analytics_data)

    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def current_user(self, request):
        user = request.user
        is_admin = user.is_staff

        return Response({
            "user_id": user.id,
            'username': user.username,
            'email': user.email,
            'is_admin': is_admin
        })


class LandingPageViewSet(viewsets.ModelViewSet):
    queryset = LandingPage.objects.all()
    serializer_class = LandingPageSerializer

    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def user_landing_page(self, request):
        landing_page = LandingPage.objects.first()
        if landing_page:
            return Response(LandingPageSerializer(landing_page).data)
        return Response({"message": "No se encontró ninguna landing page"}, status=404)
