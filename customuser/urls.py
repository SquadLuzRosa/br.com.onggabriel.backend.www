from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomUserModelViewSet


router = DefaultRouter()
router.register(r'user', CustomUserModelViewSet, basename='user_authentication')

urlpatterns = [
    path('', include(router.urls)),
]
