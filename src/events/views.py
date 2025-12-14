from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from events.models import Address, Event, EventMediaRelation, EventType
from events.serializers import (
    AddressSerializer,
    EventsSerializer,
    EventTypeSerializer,
    EventMediaRelationSerializer,
    EventMediaRelationWriteSerializer,
    EventMediaUploadSerializer,
)
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

    @action(detail=True, methods=['post'], url_path='set-cover')
    def set_cover(self, request, pk=None):
        event = self.get_object()
        media_id = request.data.get('media_id')

        if not media_id:
            return Response({'errors': 'media_id é obrigatório.'}, status=400)

        relation = EventMediaRelation.objects.filter(event=event, media_id=media_id).first()

        if not relation:
            return Response({'errors': 'Essa mídia não pertence ao evento.'}, status=400)

        relation.is_cover = True
        relation.save()

        return Response({'success': True}, status=200)

    @action(detail=True, methods=['get'], url_path='medias')
    def list_medias(self, request, pk=None):
        """Lista todas as mídias do evento"""
        event = self.get_object()
        relations = EventMediaRelation.objects.filter(event=event).select_related('media')
        serializer = EventMediaRelationSerializer(relations, many=True, context={'request': request})
        return Response(serializer.data)

    @action(detail=True, methods=['post'], url_path='medias/add')
    def add_media(self, request, pk=None):
        """Adiciona uma mídia existente ao evento"""
        event = self.get_object()
        serializer = EventMediaRelationWriteSerializer(
            data=request.data,
            context={'request': request, 'event': event}
        )
        serializer.is_valid(raise_exception=True)

        media = serializer.validated_data.get('media')
        if EventMediaRelation.objects.filter(event=event, media=media).exists():
            return Response(
                {'errors': 'Essa mídia já está vinculada ao evento.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        relation = serializer.save()
        output_serializer = EventMediaRelationSerializer(relation, context={'request': request})
        return Response(output_serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['post'], url_path='medias/upload')
    def upload_media(self, request, pk=None):
        event = self.get_object()
        serializer = EventMediaUploadSerializer(
            data=request.data,
            context={'request': request, 'event': event}
        )
        serializer.is_valid(raise_exception=True)
        relation = serializer.save()
        output_serializer = EventMediaRelationSerializer(relation, context={'request': request})
        return Response(output_serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['patch'], url_path=r'medias/(?P<relation_id>[0-9a-f-]{36})')
    def update_media(self, request, pk=None, relation_id=None):
        event = self.get_object()
        relation = EventMediaRelation.objects.filter(event=event, id=relation_id).first()

        if not relation:
            return Response(
                {'errors': 'Mídia não encontrada neste evento.'},
                status=status.HTTP_404_NOT_FOUND
            )

        is_cover = request.data.get('is_cover')
        if is_cover is not None:
            relation.is_cover = is_cover in [True, 'true', 'True', '1', 1]
            relation.save()

        output_serializer = EventMediaRelationSerializer(relation, context={'request': request})
        return Response(output_serializer.data)

    @action(detail=True, methods=['delete'], url_path=r'medias/(?P<relation_id>[0-9a-f-]{36})/remove')
    def remove_media(self, request, pk=None, relation_id=None):
        """Remove uma mídia do evento (apenas a relação, não deleta a mídia)"""
        event = self.get_object()
        relation = EventMediaRelation.objects.filter(event=event, id=relation_id).first()

        if not relation:
            return Response(
                {'errors': 'Mídia não encontrada neste evento.'},
                status=status.HTTP_404_NOT_FOUND
            )

        relation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
