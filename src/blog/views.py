from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

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


class CategoryModelViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filterset_class = CategoryFilter
