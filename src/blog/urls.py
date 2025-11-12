from django.urls import path, include
from rest_framework.routers import DefaultRouter

from blog.views import PostModelViewSet, CategoryModelViewSet

router = DefaultRouter()
router.register(r'post', PostModelViewSet, basename='post')
router.register(r'category', CategoryModelViewSet, basename='category')

urlpatterns = [
    path('', include(router.urls))
]
