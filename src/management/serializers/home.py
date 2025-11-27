from rest_framework import serializers

from management.models import (
    ManagementMedia,
    PresentationSection,
    MissionSection,
    DonateSection,
    StatsCard,
    VolunteerSection,
    DepoimentCard,
    ActivityCard,
    ContactSection,
    TributeSection,
)
from testmonial.models import Depoiment
from .media import ManagementMediaSerializer


class PresentationSectionSerializer(serializers.ModelSerializer):
    image = ManagementMediaSerializer(required=False, allow_null=True)
    image_id = serializers.PrimaryKeyRelatedField(
        queryset=ManagementMedia.objects.all(),
        source='image',
        write_only=True,
        required=False,
        allow_null=True
    )

    class Meta:
        model = PresentationSection
        fields = [
            'id',
            'top_text',
            'main_text',
            'description',
            'image',
            'image_id',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['created_at', 'updated_at']

    def create(self, validated_data):
        image_data = validated_data.pop('image', None)

        if image_data:
            image = ManagementMedia.objects.create(**image_data)
            validated_data['image'] = image
        return super().create(validated_data)

    def update(self, instance, validated_data):
        image_data = validated_data.pop('image', None)

        if image_data:
            if instance.image:
                for attr, value in image_data.items():
                    setattr(instance.image, attr, value)
                instance.image.save()
            else:
                image = ManagementMedia.objects.create(**image_data)
                validated_data['image'] = image

        return super().update(instance, validated_data)


class MissionSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MissionSection
        fields = [
            'id',
            'first_text',
            'second_text',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['created_at', 'updated_at']


class DonateSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonateSection
        fields = [
            'id',
            'main_text',
            'description',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['created_at', 'updated_at']


class StatsCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatsCard
        fields = [
            'id',
            'card_number',
            'stats_number',
            'text',
            'visible',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['created_at', 'updated_at']


class VolunteerSectionSerializer(serializers.ModelSerializer):
    image = ManagementMediaSerializer(required=False, allow_null=True)
    image_id = serializers.PrimaryKeyRelatedField(
        queryset=ManagementMedia.objects.all(),
        source='image',
        write_only=True,
        required=False,
        allow_null=True
    )

    class Meta:
        model = VolunteerSection
        fields = [
            'id',
            'title',
            'subtitle',
            'first_text',
            'second_text',
            'image',
            'image_id',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['created_at', 'updated_at']

    def create(self, validated_data):
        image_data = validated_data.pop('image', None)

        if image_data:
            image = ManagementMedia.objects.create(**image_data)
            validated_data['image'] = image
        return super().create(validated_data)

    def update(self, instance, validated_data):
        image_data = validated_data.pop('image', None)

        if image_data:
            if instance.image:
                for attr, value in image_data.items():
                    setattr(instance.image, attr, value)
                instance.image.save()
            else:
                image = ManagementMedia.objects.create(**image_data)
                validated_data['image'] = image

        return super().update(instance, validated_data)


class DepoimentCardSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        from testmonial.serializers import DepoimentSerializer  # noqa: F811, PLC0415
        data = super().to_representation(instance)
        data['depoiment'] = DepoimentSerializer(instance.depoiment, context=self.context).data if instance.depoiment else None
        return data

    depoiment_id = serializers.PrimaryKeyRelatedField(
        queryset=Depoiment.objects.all(),
        source='depoiment',
        write_only=True,
        required=False,
        allow_null=True
    )

    class Meta:
        model = DepoimentCard
        fields = [
            'id',
            'card_number',
            'depoiment',
            'depoiment_id',
            'visible',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['created_at', 'updated_at']


class ActivityCardSerializer(serializers.ModelSerializer):
    image = ManagementMediaSerializer(required=False, allow_null=True)
    image_id = serializers.PrimaryKeyRelatedField(
        queryset=ManagementMedia.objects.all(),
        source='image',
        write_only=True,
        required=False,
        allow_null=True
    )

    class Meta:
        model = ActivityCard
        fields = [
            'id',
            'card_number',
            'visible',
            'title',
            'description',
            'image',
            'image_id',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['created_at', 'updated_at']

    def create(self, validated_data):
        image_data = validated_data.pop('image', None)

        if image_data:
            image = ManagementMedia.objects.create(**image_data)
            validated_data['image'] = image
        return super().create(validated_data)

    def update(self, instance, validated_data):
        image_data = validated_data.pop('image', None)

        if image_data:
            if instance.image:
                for attr, value in image_data.items():
                    setattr(instance.image, attr, value)
                instance.image.save()
            else:
                image = ManagementMedia.objects.create(**image_data)
                validated_data['image'] = image

        return super().update(instance, validated_data)


class ContactSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactSection
        fields = [
            'id',
            'title',
            'description',
            'to_email',
            'instagram_url',
            'instagram_visible',
            'whatsapp_url',
            'whatsapp_visible',
            'twitter_url',
            'twitter_visible',
            'facebook_url',
            'facebook_visible',
            'youtube_url',
            'youtube_visible',
            'linkedin_url',
            'linkedin_visible',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['created_at', 'updated_at']


class TributeSectionSerializer(serializers.ModelSerializer):
    left_image = ManagementMediaSerializer(required=False, allow_null=True)
    left_image_id = serializers.PrimaryKeyRelatedField(
        queryset=ManagementMedia.objects.all(),
        source='left_image',
        write_only=True,
        required=False,
        allow_null=True
    )
    right_image = ManagementMediaSerializer(required=False, allow_null=True)
    right_image_id = serializers.PrimaryKeyRelatedField(
        queryset=ManagementMedia.objects.all(),
        source='right_image',
        write_only=True,
        required=False,
        allow_null=True
    )

    class Meta:
        model = TributeSection
        fields = [
            'id',
            'text',
            'left_image',
            'left_image_id',
            'right_image',
            'right_image_id',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['created_at', 'updated_at']

    def create(self, validated_data):
        left_image_data = validated_data.pop('left_image', None)
        right_image_data = validated_data.pop('right_image', None)

        if left_image_data:
            left_image = ManagementMedia.objects.create(**left_image_data)
            validated_data['left_image'] = left_image

        if right_image_data:
            right_image = ManagementMedia.objects.create(**right_image_data)
            validated_data['right_image'] = right_image

        return super().create(validated_data)

    def update(self, instance, validated_data):
        left_image_data = validated_data.pop('left_image', None)
        right_image_data = validated_data.pop('right_image', None)

        if left_image_data:
            if instance.left_image:
                for attr, value in left_image_data.items():
                    setattr(instance.left_image, attr, value)
                instance.left_image.save()
            else:
                left_image = ManagementMedia.objects.create(**left_image_data)
                validated_data['left_image'] = left_image

        if right_image_data:
            if instance.right_image:
                for attr, value in right_image_data.items():
                    setattr(instance.right_image, attr, value)
                instance.right_image.save()
            else:
                right_image = ManagementMedia.objects.create(**right_image_data)
                validated_data['right_image'] = right_image

        return super().update(instance, validated_data)


class HomePageSerializer(serializers.Serializer):
    """
    Serializer that returns all home page sections in a single response.
    """
    presentation = PresentationSectionSerializer(read_only=True)
    mission = MissionSectionSerializer(read_only=True)
    donate = DonateSectionSerializer(read_only=True)
    stats = StatsCardSerializer(many=True, read_only=True)
    volunteer = VolunteerSectionSerializer(read_only=True)
    depoiments = DepoimentCardSerializer(many=True, read_only=True)
    activities = ActivityCardSerializer(many=True, read_only=True)
    contact = ContactSectionSerializer(read_only=True)
    tribute = TributeSectionSerializer(read_only=True)
