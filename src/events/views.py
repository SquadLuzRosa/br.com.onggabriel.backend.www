from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from events.models import Address, Event, EventType
from events.serializers import AddressSerializer, EventsSerializer, EventTypeSerializer
from events.filters import AddressFilter, EventFilter, EventTypeFilter


class AddressModelViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_class = AddressFilter
    ordering_fields = ('created_at', 'updated_at', 'name')
    ordering = ('-created_at',)
    pagination_class = LimitOffsetPagination


class EventTypeModelViewSet(viewsets.ModelViewSet):
    queryset = EventType.objects.all()
    serializer_class = EventTypeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_class = EventTypeFilter
    ordering_fields = ('created_at', 'updated_at', 'name')
    ordering = ('-created_at',)
    pagination_class = LimitOffsetPagination


class EventsViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventsSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_class = EventFilter
    ordering_fields = ('event_date', 'title', 'created_at')
    pagination_class = LimitOffsetPagination
    permission_classes = [IsAuthenticatedOrReadOnly]
