from rest_framework import serializers

from testmonial.models import Depoiment, Function


class FunctionSerializer(serializers.Serializer):
    class Meta:
        model = Function
        fields = ['id', 'name', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']


class DepoimentSerializer(serializers.Serializer):
    function = FunctionSerializer(read_only=True)

    class Meta:
        model = Depoiment
        fields = [
            'id',
            'name',
            'function',
            'message',
            'cover_image',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['created_at', 'updated_at']
