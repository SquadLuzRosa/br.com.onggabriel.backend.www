from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    PostModelViewSet,
    CategoryTypeModelViewSet,
    TagModelViewSet,
    EngagementMetricsModelViewSet,
    MediaModelViewSet
)

router = DefaultRouter()
router.register(r'post', PostModelViewSet, basename='post')
router.register(r'category-type', CategoryTypeModelViewSet, basename='category-type')
router.register(r'tag', TagModelViewSet, basename='tag')
router.register(r'engagement-metrics', EngagementMetricsModelViewSet, basename='engagement-metrics')
router.register(r'media', MediaModelViewSet, basename='media')

urlpatterns = [
    path('', include(router.urls))
]
