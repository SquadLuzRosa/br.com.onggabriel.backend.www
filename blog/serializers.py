from rest_framework import serializers
from .models import (
    Post,
    CategoryType,
    Tag,
    EngagementMetrics,
    Media
)


class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class CategoryTypeSerializers(serializers.ModelSerializer):
    class Meta:
        model = CategoryType
        fields = '__all__'


class TagSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class EngagementMetricsSerializers(serializers.ModelSerializer):
    class Meta:
        model = EngagementMetrics
        fields = '__all__'


class MediaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = '__all__'
