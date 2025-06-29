from rest_framework import viewsets
from .serializer import (
    HomeSectionSerializer,
    MediaSectionSerializer,
    MissionSectionSerializer,
    AgendaSectionSerializer,
    DonationSectionSerializer,
    VoluntarySectionSerializer
)
from .models import (
    HomeSection,
    MediaSection,
    MissionSection,
    AgendaSection,
    DonationSection,
    VoluntarySection
)


class HomeSectionViewSet(viewsets.ModelViewSet):
    queryset = HomeSection.objects.all()
    serializer_class = HomeSectionSerializer


class MediaSectionViewSet(viewsets.ModelViewSet):
    queryset = MediaSection.objects.all()
    serializer_class = MediaSectionSerializer


class MissionSectionViewSet(viewsets.ModelViewSet):
    queryset = MissionSection.objects.all()
    serializer_class = MissionSectionSerializer


class AgendaSectionViewSet(viewsets.ModelViewSet):
    queryset = AgendaSection.objects.all()
    serializer_class = AgendaSectionSerializer


class DonationSectionViewSet(viewsets.ModelViewSet):
    queryset = DonationSection.objects.all()
    serializer_class = DonationSectionSerializer


class VoluntarySectionViewSet(viewsets.ModelViewSet):
    queryset = VoluntarySection.objects.all()
    serializer_class = VoluntarySectionSerializer
