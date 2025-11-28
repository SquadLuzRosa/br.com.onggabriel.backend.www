from django.urls import path, include
from rest_framework.routers import DefaultRouter

from events.views import AddressModelViewSet, EventsViewSet, EventTypeModelViewSet

router = DefaultRouter()
router.register(r'address', AddressModelViewSet, basename='address')
router.register(r'event-type', EventTypeModelViewSet, basename='event-type')
router.register(r'event', EventsViewSet, basename='event')

urlpatterns = [
    path('', include(router.urls))
]
