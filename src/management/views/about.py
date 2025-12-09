from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from management.models import (
    AboutHistorySection,
    AboutMissionSection,
    AboutValueCards,
    AboutIdealizersSection,
    AboutCarouselSection,
)
from management.serializers import (
    AboutHistorySectionSerializer,
    AboutMissionSectionSerializer,
    AboutValueCardsSerializer,
    AboutIdealizersSectionSerializer,
    AboutCarouselSectionSerializer,
    AboutPageSerializer,
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


class AboutHistorySectionViewSet(SingletonViewSetMixin, viewsets.ModelViewSet):
    """
    ViewSet for AboutHistorySection with singleton behavior.
    """
    queryset = AboutHistorySection.objects.all()
    serializer_class = AboutHistorySectionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    model = AboutHistorySection


class AboutMissionSectionViewSet(SingletonViewSetMixin, viewsets.ModelViewSet):
    """
    ViewSet for AboutMissionSection with singleton behavior.
    """
    queryset = AboutMissionSection.objects.all()
    serializer_class = AboutMissionSectionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    model = AboutMissionSection


class AboutValueCardsViewSet(viewsets.ModelViewSet):
    """
    ViewSet for AboutValueCards. Multiple instances allowed (max 7).
    """
    queryset = AboutValueCards.objects.all()
    serializer_class = AboutValueCardsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class AboutIdealizersSectionViewSet(SingletonViewSetMixin, viewsets.ModelViewSet):
    """
    ViewSet for AboutIdealizersSection with singleton behavior.
    """
    queryset = AboutIdealizersSection.objects.all()
    serializer_class = AboutIdealizersSectionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    model = AboutIdealizersSection


class AboutCarouselSectionViewSet(SingletonViewSetMixin, viewsets.ModelViewSet):
    """
    ViewSet for AboutCarouselSection with singleton behavior.
    """
    queryset = AboutCarouselSection.objects.all()
    serializer_class = AboutCarouselSectionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    model = AboutCarouselSection


class AboutPageViewSet(viewsets.ViewSet):
    """
    ViewSet that returns all about page sections in a single response.
    """
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = AboutPageSerializer

    def list(self, request):
        """
        Returns complete about page data with all sections.
        """
        data = {
            'history': None,
            'mission': None,
            'values': [],
            'idealizers': None,
            'carousel': None,
        }

        # Singleton sections
        history = AboutHistorySection.objects.first()
        if history:
            data['history'] = AboutHistorySectionSerializer(history, context={'request': request}).data

        mission = AboutMissionSection.objects.first()
        if mission:
            data['mission'] = AboutMissionSectionSerializer(mission, context={'request': request}).data

        idealizers = AboutIdealizersSection.objects.first()
        if idealizers:
            data['idealizers'] = AboutIdealizersSectionSerializer(idealizers, context={'request': request}).data

        carousel = AboutCarouselSection.objects.first()
        if carousel:
            data['carousel'] = AboutCarouselSectionSerializer(carousel, context={'request': request}).data

        # Multiple instances
        values = AboutValueCards.objects.all().order_by('card_number')
        data['values'] = AboutValueCardsSerializer(values, many=True, context={'request': request}).data

        return Response(data)
