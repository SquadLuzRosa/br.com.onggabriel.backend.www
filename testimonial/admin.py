from django.contrib import admin
from .models import Depoiment as Testimonial, MediaSection


class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'function', 'description', 'image')
    search_fields = ('name', 'function')
    list_filter = ('function',)
    ordering = ('-id',)


class MediaSectionAdmin(admin.ModelAdmin):
    list_display = ('media_type', 'description')
    search_fields = ('media_type', 'description')


admin.site.register(MediaSection, MediaSectionAdmin)
admin.site.register(Testimonial, TestimonialAdmin)
