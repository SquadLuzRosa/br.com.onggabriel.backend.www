from django.contrib import admin
from .models import CategoryType, Tag, Post, EngagementMetrics, Media


@admin.register(CategoryType)
class CategoryTypeAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'description')
    search_fields = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('title',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('title',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'author', 'publication_date')
    search_fields = ('title', 'summary', 'content')
    list_filter = ('status', 'categories', 'tags')
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ('categories', 'tags')
    date_hierarchy = 'publication_date'
    ordering = ('title', 'status', 'author')


@admin.register(EngagementMetrics)
class EngagementMetricsAdmin(admin.ModelAdmin):
    list_display = ('post', 'views', 'shares', 'comments', 'last_update')
    search_fields = ('post__title',)
    ordering = ('-views', '-shares', '-comments')


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('post', 'media_type', 'file', 'description')
    search_fields = ('post__title', 'description')
    list_filter = ('media_type',)
