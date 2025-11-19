from django.db.models import F
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from blog.filters import CategoryFilter, PostFilter
from blog.models import Category, Post
from blog.serializers import CategorySerializer, PostSerializer


class PostModelViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.select_related('author').prefetch_related('categories')
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filterset_class = PostFilter

    def perform_create(self, serializer):
        """
        Override perform_create to set the author to the current user.
        """
        serializer.save(author=self.request.user)

    def retrieve(self, request, *args, **kwargs):
        """
        Override retrieve to automatically increment view count when fetching a post by ID.
        """
        instance = self.get_object()
        Post.objects.filter(pk=instance.pk).update(views_count=F('views_count') + 1)
        instance.refresh_from_db()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        """
        Override list to increment view count when filtering by slug.
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

        return response

    @action(detail=True, methods=['post'], url_path='increment-share')
    def increment_share(self, request, pk=None):
        """
        Custom action to increment share count.
        POST /api/v1/post/{id}/increment-share/
        """
        post = self.get_object()
        Post.objects.filter(pk=post.pk).update(shares_count=F('shares_count') + 1)
        post.refresh_from_db()
        return Response({
            'shares_count': post.shares_count,
            'message': 'Share count incremented successfully'
        }, status=status.HTTP_200_OK)


class CategoryModelViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filterset_class = CategoryFilter
