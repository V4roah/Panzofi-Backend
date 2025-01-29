from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.conf import settings
from django.conf.urls.static import static

# Importaciones para drf-yasg (Swagger y Redoc)
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Configuración de la documentación de Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="Panzofi API",
        default_version="v1",
        description="Documentación de la API del proyecto Panzofi",
        terms_of_service="https://www.tusitio.com/terminos/",
        contact=openapi.Contact(email="tuemail@ejemplo.com"),
        license=openapi.License(name="Licencia MIT"),
    ),
    public=True,  # Cambia a False si solo quieres que la vean usuarios autenticados
    # Puedes cambiarlo a IsAdminUser
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("users.urls")),

    # Rutas para autenticación con JWT
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    # Rutas para la documentación de la API
    path("swagger/", schema_view.with_ui("swagger",
         cache_timeout=0), name="schema-swagger-ui"),

]

# Servir archivos multimedia en modo DEBUG
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
