from rest_framework import serializers

from events.models import Address, Event, EventMediaRelation, EventType
from management.models import ManagementMedia
from management.serializers import ManagementMediaSerializer


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = [
            'id',
            'name',
            'street',
            'number',
            'district',
            'city',
            'state',
            'zipcode',
            'google_maps_url',
            'created_at',
            'updated_at',
        ]
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
                if (
                    EventType.objects.filter(name=normalized_name)
                    .exclude(pk=instance.pk)
                    .exists()
                ):
                    raise serializers.ValidationError({
                        'errors': f'Já existe um tipo de evento com o nome "{name}".'
                    })
            elif EventType.objects.filter(name=normalized_name).exists():
                raise serializers.ValidationError({
                    'errors': f'Já existe um tipo de evento com o nome "{name}".'
                })

        return attrs


class EventMediaRelationSerializer(serializers.ModelSerializer):
    media = ManagementMediaSerializer(read_only=True)

    class Meta:
        model = EventMediaRelation
        fields = ['id', 'media', 'is_cover', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']


class EventMediaRelationWriteSerializer(serializers.ModelSerializer):
    media_id = serializers.PrimaryKeyRelatedField(
        queryset=ManagementMedia.objects.all(),
        source='media',
        write_only=True,
    )
    media = ManagementMediaSerializer(read_only=True)

    class Meta:
        model = EventMediaRelation
        fields = ['id', 'media', 'media_id', 'is_cover', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

    def create(self, validated_data):
        event = self.context.get('event')
        validated_data['event'] = event
        return super().create(validated_data)


class EventMediaUploadSerializer(serializers.Serializer):
    file = serializers.FileField()
    media_type = serializers.ChoiceField(
        choices=ManagementMedia.MEDIA_TYPES, default='image'
    )
    alt_text = serializers.CharField(max_length=255, required=False, allow_blank=True)
    title = serializers.CharField(max_length=255, required=False, allow_blank=True)
    caption = serializers.CharField(max_length=255, required=False, allow_blank=True)
    is_cover = serializers.BooleanField(default=False, required=False)

    def create(self, validated_data):
        event = self.context.get('event')
        is_cover = validated_data.pop('is_cover', False)

        management_media = ManagementMedia.objects.create(
            file=validated_data.get('file'),
            media_type=validated_data.get('media_type', 'image'),
            alt_text=validated_data.get('alt_text', ''),
            title=validated_data.get('title', ''),
            caption=validated_data.get('caption', ''),
        )

        relation = EventMediaRelation.objects.create(
            event=event,
            media=management_media,
            is_cover=is_cover,
        )

        return relation


class EventMediaWriteSerializer(serializers.Serializer):
    """Serializer para criar mídia nested no evento"""

    file = serializers.FileField()
    media_type = serializers.ChoiceField(
        choices=ManagementMedia.MEDIA_TYPES, default='image'
    )
    alt_text = serializers.CharField(max_length=255, required=False, allow_blank=True)
    title = serializers.CharField(max_length=255, required=False, allow_blank=True)
    caption = serializers.CharField(max_length=255, required=False, allow_blank=True)
    is_cover = serializers.BooleanField(default=False, required=False)


class EventsSerializer(serializers.ModelSerializer):
    # Read fields
    type = EventTypeSerializer(read_only=True)
    address = AddressSerializer(read_only=True)
    cover_media = serializers.SerializerMethodField()
    medias = serializers.SerializerMethodField()

    # Write fields
    type_id = serializers.PrimaryKeyRelatedField(
        queryset=EventType.objects.all(), source='type', write_only=True
    )
    address_id = serializers.PrimaryKeyRelatedField(
        queryset=Address.objects.all(),
        source='address',
        write_only=True,
        required=False,
        allow_null=True,
    )

    # first option: existent medias
    media_ids = serializers.PrimaryKeyRelatedField(
        queryset=ManagementMedia.objects.all(),
        many=True,
        write_only=True,
        required=False,
    )
    cover_media_id = serializers.PrimaryKeyRelatedField(
        queryset=ManagementMedia.objects.all(),
        write_only=True,
        required=False,
        allow_null=True,
    )

    class Meta:
        model = Event
        fields = [
            'id',
            'title',
            'type',
            'type_id',
            'event_date',
            'address',
            'address_id',
            'description',
            'content',
            'event_end_time',
            'is_participation',
            'online_url',
            'created_at',
            'updated_at',
            'cover_media',
            'cover_media_id',
            'medias',
            'media_ids',
        ]
        read_only_fields = ['created_at', 'updated_at']

    def get_cover_media(self, obj):
        request = self.context.get('request')
        cover = obj.media_links.filter(is_cover=True).first()
        if not cover:
            return None
        return ManagementMediaSerializer(cover.media, context={'request': request}).data

    def get_medias(self, obj):
        request = self.context.get('request')
        media_links = obj.media_links.filter(is_cover=False)
        medias = [link.media for link in media_links]
        return ManagementMediaSerializer(
            medias, many=True, context={'request': request}
        ).data

    def _parse_nested_medias(self, request):
        """
        Parse nested medias of request multipart/form-data.
        """
        medias_data = []

        if not request:
            return medias_data

        index = set()
        for key in list(request.data.keys()) + list(request.FILES.keys()):
            if key.startswith('medias['):
                try:
                    idx = int(key.split('[')[1].split(']')[0])
                    index.add(idx)
                except ValueError, IndexError:
                    continue

        for idx in sorted(index):
            media_data = {}

            for field in ['media_type', 'alt_text', 'title', 'caption', 'is_cover']:
                key = f'medias[{idx}][{field}]'
                if key in request.data:
                    value = request.data.get(key)
                    if field == 'is_cover':
                        values = ['true', 'True', '1', True]
                        media_data[field] = value in values
                    else:
                        media_data[field] = value

            file_key = f'medias[{idx}][file]'
            if file_key in request.FILES:
                media_data['file'] = request.FILES.get(file_key)

            if media_data.get('file'):
                medias_data.append(media_data)

        return medias_data

    def validate(self, attrs):
        media_ids = attrs.get('media_ids', [])
        cover_media_id = attrs.get('cover_media_id')

        if cover_media_id and media_ids and cover_media_id not in media_ids:
            raise serializers.ValidationError({
                'cover_media_id': 'A mídia de capa deve estar na lista de mídias do evento.'
            })

        return attrs

    def create(self, validated_data):
        media_ids = validated_data.pop('media_ids', [])
        cover_media_id = validated_data.pop('cover_media_id', None)

        # parse nested medias on request
        request = self.context.get('request')
        nested_medias = self._parse_nested_medias(request)

        instance = super().create(validated_data)

        # process nested medias
        created_medias = []
        cover_from_nested = None

        for media_data in nested_medias:
            is_cover = media_data.pop('is_cover', False)
            media_serializer = EventMediaWriteSerializer(data=media_data)
            media_serializer.is_valid(raise_exception=True)

            # management media creation
            management_media = ManagementMedia.objects.create(
                file=media_data.get('file'),
                media_type=media_data.get('media_type', 'image'),
                alt_text=media_data.get('alt_text', ''),
                title=media_data.get('title', ''),
                caption=media_data.get('caption', ''),
            )
            created_medias.append(management_media)

            if is_cover:
                cover_from_nested = management_media

        # if cover has not defined, select the first as cover
        if created_medias and not cover_from_nested:
            cover_from_nested = created_medias[0]

        # create EventMediaRelation for nested medias
        for media in created_medias:
            EventMediaRelation.objects.create(
                event=instance, media=media, is_cover=(media == cover_from_nested)
            )

        # process media_ids
        if media_ids:
            # if cover has not defined, select the first as cover
            if not cover_media_id:
                cover_media_id = media_ids[0]

            for media in media_ids:
                # just select as cover if this event hasnt cover
                is_cover = (media == cover_media_id) and not cover_from_nested
                EventMediaRelation.objects.create(
                    event=instance, media=media, is_cover=is_cover
                )

        return instance

    def update(self, instance, validated_data):
        media_ids = validated_data.pop('media_ids', None)
        cover_media_id = validated_data.pop('cover_media_id', None)

        # parse nested medias on request
        request = self.context.get('request')
        nested_medias = self._parse_nested_medias(request)

        instance = super().update(instance, validated_data)

        # if has new medias on nested or media ids, process
        if nested_medias or media_ids is not None:
            # remove old relations
            EventMediaRelation.objects.filter(event=instance).delete()

            # process nested medias (create new)
            created_medias = []
            cover_from_nested = None

            for media_data in nested_medias:
                is_cover = media_data.pop('is_cover', False)

                # Create ManagementMedia
                management_media = ManagementMedia.objects.create(
                    file=media_data.get('file'),
                    media_type=media_data.get('media_type', 'image'),
                    alt_text=media_data.get('alt_text', ''),
                    title=media_data.get('title', ''),
                    caption=media_data.get('caption', ''),
                )
                created_medias.append(management_media)

                if is_cover:
                    cover_from_nested = management_media

            # if cover has not defined, select the first as cover
            if created_medias and not cover_from_nested:
                cover_from_nested = created_medias[0]

            # create EventMediaRelation for nested medias
            for media in created_medias:
                EventMediaRelation.objects.create(
                    event=instance, media=media, is_cover=(media == cover_from_nested)
                )

            # process existent media_ids
            if media_ids:
                # if cover has not defined, select the first as cover
                if not cover_media_id and not cover_from_nested:
                    cover_media_id = media_ids[0]

                for media in media_ids:
                    is_cover = (media == cover_media_id) and not cover_from_nested
                    EventMediaRelation.objects.create(
                        event=instance, media=media, is_cover=is_cover
                    )

        elif cover_media_id is not None:
            # just update cover
            EventMediaRelation.objects.filter(event=instance, is_cover=True).update(
                is_cover=False
            )
            EventMediaRelation.objects.filter(
                event=instance, media=cover_media_id
            ).update(is_cover=True)

        return instance
