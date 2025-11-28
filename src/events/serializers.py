from rest_framework import serializers

from events.models import Event
from management.models import ManagementMedia
from management.serializers import ManagementMediaSerializer


class EventsSerializer(serializers.ModelSerializer):
    medias = ManagementMediaSerializer(many=True, required=False)
    media_ids = serializers.PrimaryKeyRelatedField(
        queryset=ManagementMedia.objects.all(),
        many=True,
        source='medias',
        write_only=True,
        required=False
    )

    class Meta:
        model = Event
        fields = [
            'id',
            'title',
            'type',
            'event_date',
            'address',
            'description',
            'content',
            'link',
            'event_end_time',
            'is_participation',
            'created_at',
            'updated_at',
            'medias',
            'media_ids'
        ]
    read_only_fields = ['created_at', 'updated_at']

    def create(self, validated_data):
        medias = validated_data.pop('medias', [])
        instance = super().create(validated_data)
        if medias:
            instance.medias.set(medias)
        return instance

    def update(self, instance, validated_data):
        medias = validated_data.pop('medias', None)
        instance = super().update(instance, validated_data)
        if medias is not None:
            instance.medias.set(medias)
        return instance
