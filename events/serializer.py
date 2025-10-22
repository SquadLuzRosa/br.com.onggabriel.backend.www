from rest_framework import serializers
from .models import Events


class EventsSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False, allow_null=True, use_url=True)

    class Meta:
        model = Events
        fields = [
            'id',
            'title',
            'type',
            'event_date',
            'address',
            'description',
            'content',
            'image',
            'link',
            'event_end_time',
            'is_participation',
        ]
