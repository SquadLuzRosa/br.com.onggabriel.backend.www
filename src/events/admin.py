from django.contrib import admin
from events.models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'event_date', 'is_participation', 'created_at')
    list_filter = ('type', 'is_participation', 'event_date', 'created_at')
    search_fields = ('title', 'description', 'content', 'type', 'address')
    ordering = ('-event_date', 'title')
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('title', 'type', 'description')
        }),
        ('Data e Horário', {
            'fields': ('event_date', 'event_end_time')
        }),
        ('Localização', {
            'fields': ('address', 'link')
        }),
        ('Conteúdo', {
            'fields': ('content', 'image')
        }),
        ('Configurações', {
            'fields': ('is_participation',)
        }),
        ('Metadados', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
