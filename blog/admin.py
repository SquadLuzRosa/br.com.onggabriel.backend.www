from django.contrib import admin
from .models import CategoryType, Tag, Post, EngagementMetrics, Media


@admin.register(CategoryType)
class CategoryTypeAdmin(admin.ModelAdmin):
    list_display = ('title', )
    search_fields = ('title', )
    ordering = ('title', )


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('title', )
    search_fields = ('title', )
    ordering = ('title', )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', )
    search_fields = ('title', 'content', )
    list_filter = ('categories', )
    filter_horizontal = ('categories', )
    ordering = ('title', 'author', )


@admin.register(EngagementMetrics)
class EngagementMetricsAdmin(admin.ModelAdmin):
    list_display = ('post', 'views', 'shares', 'comments', )
    search_fields = ('post__title', )
    ordering = ('-views', '-shares', '-comments', )


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('post', 'media_type', 'file', 'description', )
    search_fields = ('post__title', 'description', )
    list_filter = ('media_type', )
