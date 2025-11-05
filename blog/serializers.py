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
        fields = ['id', 'title', 'description']
        read_only_fields = ['id']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'title']


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
            'slug',
            'title',
            'content',
            'author',
            'creation_date',
            'update_date',
            'cover_image',
            'categories',
            'media_post',
            'category_ids',
        ]
        read_only_fields = ['slug', 'creation_date', 'update_date', 'author']

    def validate(self, attrs):
        request = self.context.get('request')
        author = request.user if request else None

        if author and Post.objects.filter(author=author, title=attrs.get('title')).exists():
            raise serializers.ValidationError({
                'errors': 'Você já possui um post com este título.'
            })

        return attrs


class EngagementMetricsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EngagementMetrics
        fields = '__all__'
