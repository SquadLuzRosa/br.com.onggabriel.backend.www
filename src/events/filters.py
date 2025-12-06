import django_filters
from django.db.models import Q

from events.models import Address, Event, EventType


class EventTypeFilter(django_filters.FilterSet):
    class Meta:
        model = EventType
        fields = ['id', 'name', 'created_at', 'updated_at']


class AddressFilter(django_filters.FilterSet):
    class Meta:
        model = Address
        fields = ['id', 'street', 'street', 'district', 'created_at', 'updated_at', 'city', 'state', 'zipcode']


class EventFilter(django_filters.FilterSet):
    keyword = django_filters.CharFilter(method='filter_keyword')
    title = django_filters.CharFilter(lookup_expr='icontains')
    is_participation = django_filters.BooleanFilter()
    is_virtual = django_filters.BooleanFilter(method='filter_is_virtual')

    type_id = django_filters.CharFilter(field_name='type__id', lookup_expr='iexact')
    type_name = django_filters.CharFilter(field_name='type__name', lookup_expr='icontains')

    address_id = django_filters.CharFilter(field_name='address__id', lookup_expr='iexact')
    address_name = django_filters.CharFilter(field_name='address__name', lookup_expr='icontains')

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
            'is_virtual',
        ]

    def filter_keyword(self, queryset, _name, value):
        """
        Filter events by keyword in title, description, or content.
        """
        return queryset.filter(
            Q(title__icontains=value) |
            Q(description__icontains=value) |
            Q(content__icontains=value) |
            Q(type__name__icontains=value)
        )

    def filter_is_virtual(self, queryset, _name, value):
        """
        Filter events by virtual status.
        If True, return events with online_url not null/empty.
        If False, return events with address not null.
        """
        if value:
            return queryset.filter(
                ~Q(online_url__isnull=True) & ~Q(online_url='')
            )
        else:
            return queryset.filter(address__isnull=False)
