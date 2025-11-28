from django.contrib import admin
from events.models import Address, Event, EventType


@admin.register(EventType)
class EventTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'description')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('name',)

    fieldsets = (
        ('Informações do Tipo', {
            'fields': ('name', 'description')
        }),
        ('Metadados', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('name', 'street', 'city', 'state', 'zipcode', 'created_at')
    list_filter = ('name', 'state', 'city', 'created_at')
    search_fields = ('name', 'street', 'number', 'district', 'city', 'state', 'zipcode')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('name',)

    fieldsets = (
        ('Endereço', {
            'fields': ('name', 'street', 'number', 'district', 'city', 'state', 'zipcode')
        }),
        ('Google Maps', {
            'fields': ('google_maps_url',)
        }),
        ('Metadados', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


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
            'fields': ('address',)
        }),
        ('Conteúdo', {
            'fields': ('content', 'medias')
        }),
        ('Configurações', {
            'fields': ('is_participation',)
        }),
        ('Metadados', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
