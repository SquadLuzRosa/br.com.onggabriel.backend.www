from django.urls import path, include
from .views import EventsViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'events', EventsViewSet, basename='events')

urlpatterns = [
    path('', include(router.urls))
]
