from rest_framework import serializers

from authentication.models import CustomUser
from blog.models import Category, Post


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']


class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    categories = CategorySerializer(many=True, read_only=True)

    category_ids = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source='categories',
        many=True,
        write_only=True,
        required=False
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
            'cover_image',
            'categories',
            'category_ids',
        ]
        read_only_fields = ['slug', 'created_at', 'updated_at', 'author']
        extra_kwargs = {
            'categories': {'required': False}
        }

    def to_internal_value(self, data):
        """
        Handle both 'categories' and 'category_ids' in the payload.
        """
        # If 'categories' is in data (from form-data), rename it to 'category_ids'
        if 'categories' in data and 'category_ids' not in data:
            data = data.copy()
            categories_value = data.pop('categories')
            
            # Handle both single UUID and list of UUIDs
            if isinstance(categories_value, str):
                data['category_ids'] = [categories_value]
            elif isinstance(categories_value, list):
                data['category_ids'] = categories_value
            else:
                data['category_ids'] = [categories_value]
        
        return super().to_internal_value(data)

    def validate(self, attrs):
        request = self.context.get('request')
        author = request.user if request and request.user.is_authenticated else None

        if author and Post.objects.filter(author=author, title=attrs.get('title')).exists():
            raise serializers.ValidationError({
                'errors': 'Você já possui um post com este título.'
            })

        return attrs

    def create(self, validated_data):
        """
        Override create to handle ManyToMany relationship for categories.
        """
        categories = validated_data.pop('categories', [])
        post = Post.objects.create(**validated_data)
        post.categories.set(categories)
        return post

    def update(self, instance, validated_data):
        """
        Override update to handle ManyToMany relationship for categories.
        """
        categories = validated_data.pop('categories', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if categories is not None:
            instance.categories.set(categories)

        return instance
