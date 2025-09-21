from rest_framework import viewsets
from .models import Events
from .serializer import EventsSerializer
from .filters import EventsFilterClass


class EventsViewSet(viewsets.ModelViewSet):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer
    rql_filter_class = EventsFilterClass
