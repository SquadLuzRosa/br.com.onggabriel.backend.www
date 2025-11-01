from rest_framework import serializers
from customuser.models import CustomUser
from .models import (
    Post,
    CategoryType,
    Tag,
    EngagementMetrics,
    Media
)


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email']


class CategoryTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryType
        fields = ['id', 'title', 'slug', 'description']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'title', 'slug']


class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = ['id', 'file', 'media_type', 'description']


class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    categories = CategoryTypeSerializer(many=True, read_only=True)
    media_post = MediaSerializer(many=True, read_only=True)

    category_ids = serializers.PrimaryKeyRelatedField(
        queryset=CategoryType.objects.all(),
        source='categories',
        many=True,
        write_only=True
    )

    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'content',
            'author',
            'creation_date',
            'update_date',
            'cover_image',
            'categories',
            'tags',
            'media_post',
            'tag_ids',
            'category_ids',
        ]


class EngagementMetricsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EngagementMetrics
        fields = '__all__'
