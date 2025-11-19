import django_filters
from django.db.models import Q

from events.models import Event


class EventFilter(django_filters.FilterSet):
    keyword = django_filters.CharFilter(method='filter_keyword')
    type = django_filters.CharFilter(lookup_expr='icontains')
    title = django_filters.CharFilter(lookup_expr='icontains')
    address = django_filters.CharFilter(lookup_expr='icontains')
    is_participation = django_filters.BooleanFilter()

    event_date__gte = django_filters.DateTimeFilter(field_name='event_date', lookup_expr='gte')
    event_date__lte = django_filters.DateTimeFilter(field_name='event_date', lookup_expr='lte')
    created_at__gte = django_filters.DateTimeFilter(field_name='created_at', lookup_expr='gte')
    created_at__lte = django_filters.DateTimeFilter(field_name='created_at', lookup_expr='lte')

    class Meta:
        model = Event
        fields = [
            'id',
            'type',
            'title',
            'address',
            'is_participation',
        ]

    def filter_keyword(self, queryset, _name, value):
        """
        Filter events by keyword in title, description, or content.
        """
        return queryset.filter(
            Q(title__icontains=value) |
            Q(description__icontains=value) |
            Q(content__icontains=value) |
            Q(type__icontains=value)
        )
