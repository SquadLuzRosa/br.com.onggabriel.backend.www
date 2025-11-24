import django_filters
from django.conf import settings
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from django.db.models import Q

from testmonial.models import Depoiment, Function


class FunctionFilter(django_filters.FilterSet):
    created_at__gt = django_filters.DateTimeFilter(field_name='created_at', lookup_expr='gt')
    created_at__lt = django_filters.DateTimeFilter(field_name='created_at', lookup_expr='lt')
    updated_at__gt = django_filters.DateTimeFilter(field_name='updated_at', lookup_expr='gt')
    updated_at__lt = django_filters.DateTimeFilter(field_name='updated_at', lookup_expr='lt')

    class Meta:
        model = Function
        fields = ['id', 'name', 'created_at', 'updated_at']


class DepoimentFilter(django_filters.FilterSet):
    keyword = django_filters.CharFilter(method='filter_keyword')

    created_at__gt = django_filters.DateTimeFilter(field_name='created_at', lookup_expr='gt')
    created_at__lt = django_filters.DateTimeFilter(field_name='created_at', lookup_expr='lt')
    updated_at__gt = django_filters.DateTimeFilter(field_name='updated_at', lookup_expr='gt')
    updated_at__lt = django_filters.DateTimeFilter(field_name='updated_at', lookup_expr='lt')

    class Meta:
        model = Depoiment
        fields = ['id', 'name', 'function', 'message', 'created_at', 'updated_at']

    def filter_keyword(self, queryset, _name, value):
        """
        Filter depoiments by keyword in message.
        Use PostgreSQL full text search when available, otherwise fallback to icontains.
        """
        if 'postgresql' in settings.DATABASES['default']['ENGINE']:
            search_vector = SearchVector('message', weight='A')
            search_query = SearchQuery(value)

            return (
                queryset
                .annotate(rank=SearchRank(search_vector, search_query))
                .filter(Q(message__icontains=value))
                .order_by('-rank')
            )

        return queryset.filter(Q(message__icontains=value))
