from django.db.models import F
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from blog.filters import CategoryFilter, PostFilter
from blog.models import Category, Post
from blog.serializers import CategorySerializer, PostSerializer


class PostModelViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.select_related('author').prefetch_related('categories')
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_class = PostFilter
    ordering_fields = ('views_count', 'shares_count', 'created_at', 'updated_at', 'title')
    ordering = ('-created_at',)
    pagination_class = LimitOffsetPagination

    lookup_field = 'slug'
    lookup_value_regex = '[^/]+'

    def perform_create(self, serializer):
        """
        Override perform_create to set the author to the current user.
        """
        serializer.save(author=self.request.user)

    def retrieve(self, request, *args, **kwargs):
        """
        Override retrieve to automatically increment view count when fetching a post by ID.
        Also increments view count for all categories associated with the post.
        """
        instance = self.get_object()
        Post.objects.filter(pk=instance.pk).update(views_count=F('views_count') + 1)

        category_ids = instance.categories.values_list('id', flat=True)
        if category_ids:
            Category.objects.filter(id__in=category_ids).update(views_count=F('views_count') + 1)

        instance.refresh_from_db()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        """
        Override list to increment view count when filtering by slug.
        Also increments view count for all categories associated with the post.
        """
        response = super().list(request, *args, **kwargs)

        slug = request.query_params.get('slug')
        if slug and isinstance(response.data, dict) and response.data.get('count') == 1:
            results = response.data.get('results', [])
            if results:
                post_id = results[0]['id']
                Post.objects.filter(pk=post_id).update(views_count=F('views_count') + 1)
                post = Post.objects.get(pk=post_id)
                results[0]['views_count'] = post.views_count

                category_ids = post.categories.values_list('id', flat=True)
                if category_ids:
                    Category.objects.filter(id__in=category_ids).update(views_count=F('views_count') + 1)

        return response

    @action(detail=True, methods=['post'], url_path='increment-share')
    def increment_share(self, request, slug=None):
        """
        Custom action to increment share count.
        POST /api/v1/post/{slug}/increment-share/
        """
        post = self.get_object()
        Post.objects.filter(pk=post.pk).update(shares_count=F('shares_count') + 1)
        post.refresh_from_db()
        return Response({
            'shares_count': post.shares_count,
            'message': 'Share count incremented successfully'
        }, status=status.HTTP_200_OK)

    @action(detail=True, methods=['get'], url_path='related')
    def related(self, request, slug=None):
        """
        Returns up to 6 related posts: 3 most viewed and 3 most recent.
        Excludes the current post (by slug).
        GET /api/v1/post/{slug}/related/
        """
        current_post = self.get_object()

        most_viewed = Post.objects.exclude(pk=current_post.pk).order_by('-views_count')[:3]
        most_recent = Post.objects.exclude(pk=current_post.pk).order_by('-created_at')[:3]

        most_viewed_serializer = self.get_serializer(most_viewed, many=True)
        most_recent_serializer = self.get_serializer(most_recent, many=True)

        return Response({
            'most_viewed': most_viewed_serializer.data,
            'most_recent': most_recent_serializer.data
        }, status=status.HTTP_200_OK)


class CategoryModelViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_class = CategoryFilter
    ordering_fields = ('views_count', 'created_at', 'updated_at', 'name')
    ordering = ('-created_at',)
    pagination_class = LimitOffsetPagination
