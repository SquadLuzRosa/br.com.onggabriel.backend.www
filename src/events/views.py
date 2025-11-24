from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from events.models import Event
from events.serializers import EventsSerializer
from events.filters import EventFilter


class EventsViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventsSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_class = EventFilter
    ordering_fields = ('event_date', 'title', 'created_at')
    pagination_class = LimitOffsetPagination
    permission_classes = [IsAuthenticatedOrReadOnly]
