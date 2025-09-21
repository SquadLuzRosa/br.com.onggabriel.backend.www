from django.contrib import admin
from .models import Events


@admin.register(Events)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('title', 'event_date', 'address', 'created_at')
    list_filter = ('event_date',)
    search_fields = ('title', 'description', 'address')
    ordering = ('-event_date',)
