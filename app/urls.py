from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView
)
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('api/v1/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/v1/swagger/', SpectacularSwaggerView.as_view(), name='swagger'),
    path('api/v1/redoc/', SpectacularRedocView.as_view(), name='redoc'),

    path('api/v1/', include('authentication.urls')),
    path('api/v1/', include('customuser.urls')),
    path('api/v1/', include('blog.urls')),

    path('api/v1/', include('testimonial.urls')),
    path('api/v1/', include('management.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
