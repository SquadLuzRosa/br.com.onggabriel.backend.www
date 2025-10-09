from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import LimitOffsetPagination
from .models import Events
from .serializer import EventsSerializer
from .filters import EventsFilterClass


class EventsViewSet(viewsets.ModelViewSet):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer
    filter_backends = (OrderingFilter, )
    ordering_fields = ('event_date', 'title', 'created_at')
    pagination_class = LimitOffsetPagination
    rql_filter_class = EventsFilterClass
