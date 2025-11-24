from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from testmonial.filters import DepoimentFilter, FunctionFilter
from testmonial.models import Depoiment, Function
from testmonial.serializers import DepoimentSerializer, FunctionSerializer


class FunctionModelViewSet(viewsets.ModelViewSet):
    queryset = Function.objects.all()
    serializer_class = FunctionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_class = FunctionFilter
    ordering_fields = ('created_at', 'updated_at', 'name')
    ordering = ('-created_at',)
    pagination_class = LimitOffsetPagination


class DepoimentModelViewSet(viewsets.ModelViewSet):
    queryset = Depoiment.objects.all().select_related('function')
    serializer_class = DepoimentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_class = DepoimentFilter
    ordering_fields = ('created_at', 'updated_at', 'name')
    ordering = ('-created_at',)
    pagination_class = LimitOffsetPagination
