from rest_framework import viewsets
from .models import Events
from .serializer import EventsSerializer


class EventsViewSet(viewsets.ModelViewSet):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer
