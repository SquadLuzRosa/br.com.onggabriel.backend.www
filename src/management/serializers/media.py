from rest_framework import serializers

from management.models import ManagementMedia


class ManagementMediaSerializer(serializers.ModelSerializer):
    file = serializers.SerializerMethodField()

    class Meta:
        model = ManagementMedia
        fields = ['id', 'file', 'media_type', 'alt_text', 'title', 'caption', 'slug']
        read_only_fields = ['slug']

    def get_file(self, obj: ManagementMedia) -> str:
        """Return full url"""
        if obj.file:
            request = self.context.get('request')
            if request is not None:
                return request.build_absolute_uri(obj.file.url)
            return obj.file.url
        return None
