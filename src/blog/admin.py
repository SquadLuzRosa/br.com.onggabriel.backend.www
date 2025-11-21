from django.contrib import admin
from .models import Category, Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )
    ordering = ('name', )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', )
    search_fields = ('title', 'content', )
    list_filter = ('categories', )
    filter_horizontal = ('categories', )
    ordering = ('title', 'author', )
