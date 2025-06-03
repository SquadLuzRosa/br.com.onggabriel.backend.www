from django.contrib import admin
from .models import (
    HomeSection,
    MissionSection,
    AgendaSection,
    DonationSection,
    VoluntarySection,
    MediaSection
)


class HomeSectionAdmin(admin.ModelAdmin):
    list_display = ('intro_text', 'description_text', 'image')


class MissionSectionAdmin(admin.ModelAdmin):
    list_display = ('first_text', 'second_text')


class AgendaSectionAdmin(admin.ModelAdmin):
    list_display = ('theme', 'description', 'image')


class DonationSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image')


class VoluntarySectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'sub_title', 'description', 'image')


class MediaSectionAdmin(admin.ModelAdmin):
    list_display = ('media_type', 'description')


admin.site.register(MediaSection, MediaSectionAdmin)
admin.site.register(MissionSection, MissionSectionAdmin)
admin.site.register(AgendaSection, AgendaSectionAdmin)
admin.site.register(DonationSection, DonationSectionAdmin)
admin.site.register(VoluntarySection, VoluntarySectionAdmin)
admin.site.register(HomeSection, HomeSectionAdmin)
