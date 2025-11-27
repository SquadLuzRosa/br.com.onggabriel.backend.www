from rest_framework import serializers

from management.serializers import ManagementMediaSerializer
from management.models.media import ManagementMedia
from testmonial.models import Depoiment, Function


class FunctionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Function
        fields = ['id', 'name', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']


class DepoimentSerializer(serializers.ModelSerializer):
    image = ManagementMediaSerializer(required=False, allow_null=True)
    image_id = serializers.PrimaryKeyRelatedField(
        queryset=ManagementMedia.objects.all(),
        source='image',
        write_only=True,
        required=False,
        allow_null=True
    )

    function = FunctionSerializer(read_only=True)
    function_id = serializers.PrimaryKeyRelatedField(
        queryset=Function.objects.all(),
        source='function',
        write_only=True
    )

    class Meta:
        model = Depoiment
        fields = [
            'id',
            'name',
            'function',
            'function_id',
            'message',
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
