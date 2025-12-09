from rest_framework import serializers

from management.models import (
    ManagementMedia,
    AboutHistorySection,
    AboutMissionSection,
    AboutValueCards,
    AboutIdealizersSection,
    AboutCarouselSection,
)
from .media import ManagementMediaSerializer


class AboutHistorySectionSerializer(serializers.ModelSerializer):
    card_media = ManagementMediaSerializer(read_only=True)
    card_media_id = serializers.PrimaryKeyRelatedField(
        queryset=ManagementMedia.objects.all(),
        source='card_media',
        write_only=True,
        required=False,
        allow_null=True
    )
    background_image = ManagementMediaSerializer(read_only=True)
    background_image_id = serializers.PrimaryKeyRelatedField(
        queryset=ManagementMedia.objects.all(),
        source='background_image',
        write_only=True,
        required=False,
        allow_null=True
    )

    class Meta:
        model = AboutHistorySection
        fields = [
            'id',
            'main_text',
            'description',
            'card_media',
            'card_media_id',
            'background_image',
            'background_image_id',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['created_at', 'updated_at']


class AboutMissionSectionSerializer(serializers.ModelSerializer):
    media = ManagementMediaSerializer(read_only=True)
    media_id = serializers.PrimaryKeyRelatedField(
        queryset=ManagementMedia.objects.all(),
        source='media',
        write_only=True,
        required=False,
        allow_null=True
    )

    class Meta:
        model = AboutMissionSection
        fields = [
            'id',
            'text_1',
            'text_2',
            'media',
            'media_id',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['created_at', 'updated_at']


class AboutValueCardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutValueCards
        fields = [
            'id',
            'card_number',
            'stats_number',
            'text',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['created_at', 'updated_at']


class AboutIdealizersSectionSerializer(serializers.ModelSerializer):
    media = ManagementMediaSerializer(read_only=True)
    media_id = serializers.PrimaryKeyRelatedField(
        queryset=ManagementMedia.objects.all(),
        source='media',
        write_only=True,
        required=False,
        allow_null=True
    )

    class Meta:
        model = AboutIdealizersSection
        fields = [
            'id',
            'main_text',
            'idealizers',
            'descrption',
            'media',
            'media_id',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['created_at', 'updated_at']


class AboutCarouselSectionSerializer(serializers.ModelSerializer):
    medias = ManagementMediaSerializer(many=True, read_only=True)
    media_ids = serializers.PrimaryKeyRelatedField(
        queryset=ManagementMedia.objects.all(),
        many=True,
        write_only=True,
        required=False
    )

    class Meta:
        model = AboutCarouselSection
        fields = [
            'id',
            'medias',
            'media_ids',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['created_at', 'updated_at']

    def create(self, validated_data):
        media_ids = validated_data.pop('media_ids', [])
        instance = super().create(validated_data)
        if media_ids:
            instance.medias.set(media_ids)
        return instance

    def update(self, instance, validated_data):
        media_ids = validated_data.pop('media_ids', None)
        instance = super().update(instance, validated_data)
        if media_ids is not None:
            instance.medias.set(media_ids)
        return instance


class AboutPageSerializer(serializers.Serializer):
    """
    Serializer that returns all about page sections in a single response.
    """
    history = AboutHistorySectionSerializer(read_only=True)
    mission = AboutMissionSectionSerializer(read_only=True)
    values = AboutValueCardsSerializer(many=True, read_only=True)
    idealizers = AboutIdealizersSectionSerializer(read_only=True)
    carousel = AboutCarouselSectionSerializer(read_only=True)
