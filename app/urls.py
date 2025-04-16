from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView
)


urlpatterns = [
    path('api/v1/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/v1/swagger/', SpectacularSwaggerView.as_view(), name='swagger'),
    path('api/v1/redoc/', SpectacularRedocView.as_view(), name='redoc'),

    path('api/v1/', include('authentication.urls')),
    path('admin/', admin.site.urls),
]
