from django.contrib import admin
from .models import Category, Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )
    ordering = ('name', )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'author',
        'media',
        'created_at',
        'updated_at',
        'views_count',
        'shares_count',
    )

    list_filter = (
        'author',
        'categories',
        'created_at',
    )

    search_fields = (
        'title',
        'content',
        'meta_description',
    )

    ordering = ('-created_at', 'title')

    readonly_fields = (
        'slug',
        'views_count',
        'shares_count',
        'created_at',
        'updated_at',
    )

    filter_horizontal = ('categories',)

    fieldsets = (
        ('Informações Básicas', {
            'fields': ('title', 'author', 'slug')
        }),

        ('Conteúdo', {
            'fields': ('content', 'meta_description')
        }),

        ('Mídia', {
            'fields': ('media',)
        }),

        ('Categorias', {
            'fields': ('categories',)
        }),

        ('Engajamento', {
            'fields': ('views_count', 'shares_count')
        }),

        ('Metadados', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
