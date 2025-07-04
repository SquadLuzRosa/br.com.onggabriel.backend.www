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
from .filters import (
    PostFilterClass,
    CategoryTypeFilterClass,
    TagFilterClass,
    EngagementMetricsFilterClass,
    MediaFilterClass
)


class PostModelViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.select_related('author').prefetch_related('categories', 'tags', 'media_post')
    serializer_class = PostSerializers
    rql_filter_class = PostFilterClass
    permission_classes = [IsAuthenticatedOrReadOnly]


class CategoryTypeModelViewSet(viewsets.ModelViewSet):
    queryset = CategoryType.objects.all()
    serializer_class = CategoryTypeSerializers
    rql_filter_class = CategoryTypeFilterClass
    permission_classes = [IsAuthenticatedOrReadOnly]


class TagModelViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializers
    rql_filter_class = TagFilterClass
    permission_classes = [IsAuthenticatedOrReadOnly]


class EngagementMetricsModelViewSet(viewsets.ModelViewSet):
    queryset = EngagementMetrics.objects.all()
    serializer_class = EngagementMetricsSerializers
    rql_filter_class = EngagementMetricsFilterClass
    permission_classes = [IsAuthenticatedOrReadOnly]


class MediaModelViewSet(viewsets.ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaSerializers
    rql_filter_class = MediaFilterClass
    permission_classes = [IsAuthenticatedOrReadOnly]
