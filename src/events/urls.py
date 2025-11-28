from django.urls import path, include
from rest_framework.routers import DefaultRouter

from events.views import AddressModelViewSet, EventsViewSet, EventTypeModelViewSet

router = DefaultRouter()
router.register(r'event', AddressModelViewSet, basename='event')
router.register(r'event-type', EventTypeModelViewSet, basename='event-type')
router.register(r'address', EventsViewSet, basename='address')

urlpatterns = [
    path('', include(router.urls))
]
