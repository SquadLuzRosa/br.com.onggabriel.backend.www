from rest_framework import serializers

from management.models import ManagementMedia


class ManagementMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManagementMedia
        fields = ['id', 'file', 'media_type', 'alt_text', 'title', 'caption', 'slug']
        read_only_fields = ['slug']
