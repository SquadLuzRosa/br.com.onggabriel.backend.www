from django.contrib import admin

from testmonial.models import Depoiment


@admin.register(Depoiment)
class DepoimentAdmin(admin.ModelAdmin):
    list_display = ('name', 'function', 'created_at')
    search_fields = ('name', 'function', 'description')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-created_at',)
