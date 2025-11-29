from rest_framework import serializers

from authentication.models import CustomUser
from blog.models import Category, Post
from management.models import ManagementMedia
from management.serializers import ManagementMediaSerializer


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'views_count', 'created_at', 'updated_at']
        read_only_fields = ['views_count', 'created_at', 'updated_at']

    def validate(self, attrs):
        """
        Validate that category name is unique (case-insensitive).
        """
        name = attrs.get('name')
        if name:
            normalized_name = name.lower()
            instance = self.instance

            if instance:
                if Category.objects.filter(name=normalized_name).exclude(pk=instance.pk).exists():
                    raise serializers.ValidationError({
                        'errors': f'Já existe uma categoria com o nome "{name}".'
                    })
            elif Category.objects.filter(name=normalized_name).exists():
                raise serializers.ValidationError({
                    'errors': f'Já existe uma categoria com o nome "{name}".'
                })

        return attrs


class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    categories = CategorySerializer(many=True, read_only=True)

    category_ids = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source='categories',
        many=True,
        write_only=True
    )

    media = ManagementMediaSerializer(required=False, allow_null=True)
    media_id = serializers.PrimaryKeyRelatedField(
        queryset=ManagementMedia.objects.all(),
        source='media',
        write_only=True,
        required=False,
        allow_null=True
    )

    class Meta:
        model = Post
        fields = [
            'id',
            'slug',
            'title',
            'content',
            'author',
            'created_at',
            'updated_at',
            'media',
            'media_id',
            'categories',
            'category_ids',
            'views_count',
            'shares_count',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['slug', 'created_at', 'updated_at', 'author', 'views_count', 'shares_count']

    def create(self, validated_data):
        categories = validated_data.pop('categories', [])

        media_data = validated_data.pop('media', None)

        if media_data:
            media = ManagementMedia.objects.create(**media_data)
            validated_data['media'] = media

        post = Post.objects.create(**validated_data)
        post.categories.set(categories)

        return post

    def update(self, instance, validated_data):
        categories = validated_data.pop('categories', None)

        media_data = validated_data.pop('media', None)

        if media_data:
            if instance.media:
                for attr, value in media_data.items():
                    setattr(instance.media, attr, value)
                instance.media.save()
            else:
                media = ManagementMedia.objects.create(**media_data)
                validated_data['media'] = media

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()

        if categories is not None:
            instance.categories.set(categories)

        return instance
