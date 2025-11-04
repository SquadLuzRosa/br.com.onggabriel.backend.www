from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomUserModelViewSet, CreateDefaultSuperuserView


router = DefaultRouter()
router.register(r'user', CustomUserModelViewSet, basename='user_authentication')

urlpatterns = [
    path('', include(router.urls)),
    path('setup/create-admin/', CreateDefaultSuperuserView.as_view(), name='create-default-admin'),
]
