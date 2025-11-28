from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from management.models import (
    PresentationSection,
    MissionSection,
    DonateSection,
    StatsCard,
    VolunteerSection,
    DepoimentCard,
    ActivityCard,
    ContactSection,
    TributeSection,
)
from management.serializers import (
    PresentationSectionSerializer,
    MissionSectionSerializer,
    DonateSectionSerializer,
    StatsCardSerializer,
    VolunteerSectionSerializer,
    DepoimentCardSerializer,
    ActivityCardSerializer,
    ContactSectionSerializer,
    TributeSectionSerializer,
    HomePageSerializer,
)


class SingletonViewSetMixin(viewsets.ModelViewSet):
    """
    Mixin for singleton viewsets that only allow one instance.
    """
    model = None

    def list(self, request, *args, **kwargs):
        instance = self.get_queryset().first()
        if instance is None:
            verbose_name = self.model._meta.verbose_name if self.model else 'seção'
            return Response(
                {'detail': f'Nenhuma {verbose_name} configurada.'},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        instance = self.get_queryset().first()
        if instance:
            serializer = self.get_serializer(instance, data=request.data, partial=False)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        instance = self.get_queryset().first()
        if not instance:
            verbose_name = self.model._meta.verbose_name if self.model else 'seção'
            return Response(
                {'detail': f'Nenhuma {verbose_name} encontrada para atualizar.'},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = self.get_serializer(instance, data=request.data, partial=False)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_queryset().first()
        if not instance:
            verbose_name = self.model._meta.verbose_name if self.model else 'seção'
            return Response(
                {'detail': f'Nenhuma {verbose_name} encontrada para atualizar.'},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_queryset().first()
        if not instance:
            verbose_name = self.model._meta.verbose_name if self.model else 'seção'
            return Response(
                {'detail': f'Nenhuma {verbose_name} encontrada para deletar.'},
                status=status.HTTP_404_NOT_FOUND
            )
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=['get'], url_path='current')
    def current(self, request):
        return self.list(request)


class PresentationSectionViewSet(SingletonViewSetMixin, viewsets.ModelViewSet):
    """
    ViewSet for PresentationSection with singleton behavior.
    """
    queryset = PresentationSection.objects.all()
    serializer_class = PresentationSectionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    model = PresentationSection


class MissionSectionViewSet(SingletonViewSetMixin, viewsets.ModelViewSet):
    """
    ViewSet for MissionSection with singleton behavior.
    """
    queryset = MissionSection.objects.all()
    serializer_class = MissionSectionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    model = MissionSection


class DonateSectionViewSet(SingletonViewSetMixin, viewsets.ModelViewSet):
    """
    ViewSet for DonateSection with singleton behavior.
    """
    queryset = DonateSection.objects.all()
    serializer_class = DonateSectionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    model = DonateSection


class StatsCardViewSet(viewsets.ModelViewSet):
    """
    ViewSet for StatsCard. Multiple instances allowed (max 4).
    """
    queryset = StatsCard.objects.all()
    serializer_class = StatsCardSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class VolunteerSectionViewSet(SingletonViewSetMixin, viewsets.ModelViewSet):
    """
    ViewSet for VolunteerSection with singleton behavior.
    """
    queryset = VolunteerSection.objects.all()
    serializer_class = VolunteerSectionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    model = VolunteerSection


class DepoimentCardViewSet(viewsets.ModelViewSet):
    """
    ViewSet for DepoimentCard. Multiple instances allowed (max 3).
    """
    queryset = DepoimentCard.objects.all()
    serializer_class = DepoimentCardSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ActivityCardViewSet(viewsets.ModelViewSet):
    """
    ViewSet for ActivityCard. Multiple instances allowed (max 3).
    """
    queryset = ActivityCard.objects.all()
    serializer_class = ActivityCardSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ContactSectionViewSet(SingletonViewSetMixin, viewsets.ModelViewSet):
    """
    ViewSet for ContactSection with singleton behavior.
    """
    queryset = ContactSection.objects.all()
    serializer_class = ContactSectionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    model = ContactSection


class TributeSectionViewSet(SingletonViewSetMixin, viewsets.ModelViewSet):
    """
    ViewSet for TributeSection with singleton behavior.
    """
    queryset = TributeSection.objects.all()
    serializer_class = TributeSectionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    model = TributeSection


class HomePageViewSet(viewsets.ViewSet):
    """
    ViewSet that returns all home page sections in a single response.
    """
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = HomePageSerializer

    def list(self, request):
        """
        Returns complete home page data with all sections.
        """
        data = {
            'presentation': None,
            'mission': None,
            'donate': None,
            'stats': [],
            'volunteer': None,
            'depoiments': [],
            'activities': [],
            'contact': None,
            'tribute': None,
        }

        # Singleton sections
        presentation = PresentationSection.objects.first()
        if presentation:
            data['presentation'] = PresentationSectionSerializer(presentation, context={'request': request}).data

        mission = MissionSection.objects.first()
        if mission:
            data['mission'] = MissionSectionSerializer(mission, context={'request': request}).data

        donate = DonateSection.objects.first()
        if donate:
            data['donate'] = DonateSectionSerializer(donate, context={'request': request}).data

        volunteer = VolunteerSection.objects.first()
        if volunteer:
            data['volunteer'] = VolunteerSectionSerializer(volunteer, context={'request': request}).data

        contact = ContactSection.objects.first()
        if contact:
            data['contact'] = ContactSectionSerializer(contact, context={'request': request}).data

        tribute = TributeSection.objects.first()
        if tribute:
            data['tribute'] = TributeSectionSerializer(tribute, context={'request': request}).data

        # Multiple instances
        stats = StatsCard.objects.filter(visible=True).order_by('card_number')
        data['stats'] = StatsCardSerializer(stats, many=True, context={'request': request}).data

        depoiments = DepoimentCard.objects.filter(visible=True).order_by('card_number')
        data['depoiments'] = DepoimentCardSerializer(depoiments, many=True, context={'request': request}).data

        activities = ActivityCard.objects.filter(visible=True).order_by('card_number')
        data['activities'] = ActivityCardSerializer(activities, many=True, context={'request': request}).data

        return Response(data)
