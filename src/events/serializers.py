from rest_framework import serializers

from events.models import Address, Event, EventType
from management.models import ManagementMedia
from management.serializers import ManagementMediaSerializer


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'name', 'street', 'number', 'district', 'city', 'state', 'zipcode', 'google_maps_url', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']


class EventTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventType
        fields = ['id', 'name', 'description', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']

    def validate(self, attrs):
        """
        Validate that category name is unique (case-insensitive).
        """
        name = attrs.get('name')
        if name:
            normalized_name = name.lower()
            instance = self.instance

            if instance:
                if EventType.objects.filter(name=normalized_name).exclude(pk=instance.pk).exists():
                    raise serializers.ValidationError({
                        'errors': f'Já existe um tipo de evento com o nome "{name}".'
                    })
            elif EventType.objects.filter(name=normalized_name).exists():
                raise serializers.ValidationError({
                    'errors': f'Já existe um tipo de evento com o nome "{name}".'
                })

        return attrs


class EventsSerializer(serializers.ModelSerializer):
    type = EventTypeSerializer(read_only=True)
    type_id = serializers.PrimaryKeyRelatedField(
        queryset=EventType.objects.all(),
        source='type',
        write_only=True
    )

    address = AddressSerializer(read_only=True)
    address_id = serializers.PrimaryKeyRelatedField(
        queryset=Address.objects.all(),
        source='address',
        write_only=True,
        required=False,
        allow_null=True
    )

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
            'event_end_time',
            'is_participation',
            'created_at',
            'updated_at',
            'medias',
            'media_ids'
        ]
        read_only_fields = ['created_at', 'updated_at']

    def create(self, validated_data):
        nested_medias = validated_data.pop('medias', [])
        instance = super().create(validated_data)

        for media_data in nested_medias:
            media = ManagementMedia.objects.create(**media_data)
            instance.medias.add(media)

        return instance

    def update(self, instance, validated_data):
        nested_medias = validated_data.pop('medias', None)
        instance = super().update(instance, validated_data)

        if nested_medias is not None:
            instance.medias.clear()
            for media_data in nested_medias:
                media = ManagementMedia.objects.create(**media_data)
                instance.medias.add(media)

        return instance
