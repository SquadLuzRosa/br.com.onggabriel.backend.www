import django_filters
from django.conf import settings
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from django.db.models import Q

from blog.models import Category, Post


class CategoryFilter(django_filters.FilterSet):
    class Meta:
        model = Category
        fields = ['id', 'name', 'created_at', 'updated_at']


class PostFilter(django_filters.FilterSet):
    keyword = django_filters.CharFilter(method='filter_keyword')

    created_at__gt = django_filters.DateTimeFilter(field_name='created_at', lookup_expr='gt')
    created_at__lt = django_filters.DateTimeFilter(field_name='created_at', lookup_expr='lt')
    updated_at__gt = django_filters.DateTimeFilter(field_name='updated_at', lookup_expr='gt')
    updated_at__lt = django_filters.DateTimeFilter(field_name='updated_at', lookup_expr='lt')

    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'author',
            'slug',
            'categories',
        ]

    def filter_keyword(self, queryset, _name, value):
        """
        Filter posts by keyword in title or content.
        Uses PostgreSQL Full Text Search when available, otherwise falls back to icontains.
        Orders by relevance: title matches first, then content matches.
        """
        if 'postgresql' in settings.DATABASES['default']['ENGINE']:
            search_vector = SearchVector('title', weight='A') + SearchVector('content', weight='B')
            search_query = SearchQuery(value)

            return queryset.annotate(
                rank=SearchRank(search_vector, search_query)
            ).filter(
                Q(title__icontains=value) | Q(content__icontains=value)
            ).order_by('-rank')
        else:
            return queryset.filter(
                Q(title__icontains=value) | Q(content__icontains=value)
            )
