from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import (
    Post,
    CategoryType,
    Tag,
    EngagementMetrics,
    Media
)
from .serializers import (
    PostSerializers,
    CategoryTypeSerializers,
    TagSerializers,
    EngagementMetricsSerializers,
    MediaSerializers
)


class PostModelViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.select_related('author').prefetch_related('categories', 'tags', 'media_post')
    serializer_class = PostSerializers
    permission_classes = [IsAuthenticatedOrReadOnly]


class CategoryTypeModelViewSet(viewsets.ModelViewSet):
    queryset = CategoryType.objects.all()
    serializer_class = CategoryTypeSerializers
    permission_classes = [IsAuthenticatedOrReadOnly]


class TagModelViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializers
    permission_classes = [IsAuthenticatedOrReadOnly]


class EngagementMetricsModelViewSet(viewsets.ModelViewSet):
    queryset = EngagementMetrics.objects.all()
    serializer_class = EngagementMetricsSerializers
    permission_classes = [IsAuthenticatedOrReadOnly]


class MediaModelViewSet(viewsets.ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaSerializers
    permission_classes = [IsAuthenticatedOrReadOnly]
