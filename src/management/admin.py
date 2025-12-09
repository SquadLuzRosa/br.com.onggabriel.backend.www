from django.contrib import admin

from management.models import (
    # Home
    ActivityCard,
    ContactSection,
    DepoimentCard,
    DonateSection,
    ManagementMedia,
    MissionSection,
    PresentationSection,
    StatsCard,
    TributeSection,
    VolunteerSection,
    # About
    AboutHistorySection,
    AboutMissionSection,
    AboutValueCards,
    AboutIdealizersSection,
    AboutCarouselSection,
)


@admin.register(ManagementMedia)
class ManagementMediaAdmin(admin.ModelAdmin):
    list_display = ('title', 'media_type', 'slug', 'created_at')
    list_filter = ('media_type', 'created_at')
    search_fields = ('title', 'alt_text', 'caption', 'slug')
    readonly_fields = ('slug', 'created_at', 'updated_at')
    ordering = ('-created_at',)

    fieldsets = (
        ('Arquivo', {
            'fields': ('file', 'media_type')
        }),
        ('Informações', {
            'fields': ('title', 'alt_text', 'caption')
        }),
        ('Metadados', {
            'fields': ('slug', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(PresentationSection)
class HomePresentationSectionAdmin(admin.ModelAdmin):
    list_display = ('main_text', 'top_text', 'created_at')
    search_fields = ('top_text', 'main_text', 'description')
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        ('Conteúdo', {
            'fields': ('top_text', 'main_text', 'description', 'image')
        }),
        ('Metadados', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def has_add_permission(self, request):
        """Additions are only allowed if there are no existing records"""
        return not PresentationSection.objects.exists()


@admin.register(MissionSection)
class MissionSectionAdmin(admin.ModelAdmin):
    list_display = ('first_text', 'second_text', 'created_at')
    search_fields = ('first_text', 'second_text')
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        ('Conteúdo', {
            'fields': ('first_text', 'second_text')
        }),
        ('Metadados', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def has_add_permission(self, request):
        return not MissionSection.objects.exists()


@admin.register(DonateSection)
class DonateSectionAdmin(admin.ModelAdmin):
    list_display = ('main_text', 'description', 'created_at')
    search_fields = ('main_text', 'description')
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        ('Conteúdo', {
            'fields': ('main_text', 'description')
        }),
        ('Metadados', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def has_add_permission(self, request):
        return not DonateSection.objects.exists()


@admin.register(StatsCard)
class StatsCardAdmin(admin.ModelAdmin):
    list_display = ('card_number', 'stats_number', 'text', 'visible', 'created_at')
    list_filter = ('card_number', 'visible', 'created_at')
    search_fields = ('text',)
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('card_number',)

    fieldsets = (
        ('Configuração do Card', {
            'fields': ('card_number', 'stats_number', 'text', 'visible')
        }),
        ('Metadados', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def has_add_permission(self, request):
        return StatsCard.objects.count() < StatsCard.MODELS_LEN


@admin.register(VolunteerSection)
class VolunteerSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'created_at')
    search_fields = ('title', 'subtitle', 'first_text', 'second_text')
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        ('Conteúdo', {
            'fields': ('title', 'subtitle', 'first_text', 'second_text', 'image')
        }),
        ('Metadados', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def has_add_permission(self, request):
        return not VolunteerSection.objects.exists()


@admin.register(DepoimentCard)
class DepoimentCardAdmin(admin.ModelAdmin):
    list_display = ('card_number', 'depoiment', 'visible', 'created_at')
    list_filter = ('card_number', 'visible', 'created_at')
    search_fields = ('depoiment__name', 'depoiment__message')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('card_number',)

    fieldsets = (
        ('Configuração do Card', {
            'fields': ('card_number', 'depoiment', 'visible')
        }),
        ('Metadados', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def has_add_permission(self, request):
        return DepoimentCard.objects.count() < DepoimentCard.MODELS_LEN


@admin.register(ContactSection)
class ContactSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at')
    search_fields = ('title', 'description')
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        ('Conteúdo', {
            'fields': ('title', 'description', 'to_email')
        }),
        ('Redes Sociais', {
            'fields': (
                'instagram_url', 'instagram_visible',
                'whatsapp_url', 'whatsapp_visible',
                'twitter_url', 'twitter_visible',
                'facebook_url', 'facebook_visible',
                'youtube_url', 'youtube_visible',
                'linkedin_url', 'linkedin_visible',
            )
        }),
        ('Metadados', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def has_add_permission(self, request):
        return not ContactSection.objects.exists()


@admin.register(TributeSection)
class TributeSectionAdmin(admin.ModelAdmin):
    list_display = ('text', 'created_at')
    search_fields = ('text',)
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        ('Conteúdo', {
            'fields': ('text', 'left_image', 'right_image')
        }),
        ('Metadados', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def has_add_permission(self, request):
        return not TributeSection.objects.exists()


@admin.register(ActivityCard)
class ActivityCardAdmin(admin.ModelAdmin):
    list_display = ('card_number', 'title', 'visible', 'created_at')
    list_filter = ('card_number', 'visible', 'created_at')
    search_fields = ('title', 'description')
    ordering = ('card_number',)

    fieldsets = (
        ('Configuração do Card', {
            'fields': ('card_number', 'visible')
        }),
        ('Conteúdo', {
            'fields': ('title', 'description', 'image')
        }),
        ('Metadados', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    readonly_fields = ('created_at', 'updated_at')

    def has_add_permission(self, request):
        if ActivityCard.objects.count() >= ActivityCard.MODELS_LEN:
            return False
        return super().has_add_permission(request)


# =====================
# ABOUT PAGE ADMIN
# =====================

@admin.register(AboutHistorySection)
class AboutHistorySectionAdmin(admin.ModelAdmin):
    list_display = ('main_text', 'created_at')
    search_fields = ('main_text', 'description')
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        ('Conteúdo', {
            'fields': ('main_text', 'description')
        }),
        ('Mídias', {
            'fields': ('card_media', 'background_image')
        }),
        ('Metadados', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def has_add_permission(self, request):
        return not AboutHistorySection.objects.exists()


@admin.register(AboutMissionSection)
class AboutMissionSectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at')
    search_fields = ('text_1', 'text_2')
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        ('Conteúdo', {
            'fields': ('text_1', 'text_2', 'media')
        }),
        ('Metadados', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def has_add_permission(self, request):
        return not AboutMissionSection.objects.exists()


@admin.register(AboutValueCards)
class AboutValueCardsAdmin(admin.ModelAdmin):
    list_display = ('card_number', 'stats_number', 'text', 'created_at')
    list_filter = ('card_number', 'created_at')
    search_fields = ('text',)
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('card_number',)

    fieldsets = (
        ('Configuração do Card', {
            'fields': ('card_number', 'stats_number', 'text')
        }),
        ('Metadados', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def has_add_permission(self, request):
        return AboutValueCards.objects.count() < AboutValueCards.MODELS_LEN


@admin.register(AboutIdealizersSection)
class AboutIdealizersSectionAdmin(admin.ModelAdmin):
    list_display = ('main_text', 'idealizers', 'created_at')
    search_fields = ('main_text', 'idealizers', 'descrption')
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        ('Conteúdo', {
            'fields': ('main_text', 'idealizers', 'descrption', 'media')
        }),
        ('Metadados', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def has_add_permission(self, request):
        return not AboutIdealizersSection.objects.exists()


@admin.register(AboutCarouselSection)
class AboutCarouselSectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_medias_count', 'created_at')
    readonly_fields = ('created_at', 'updated_at')
    filter_horizontal = ('medias',)

    fieldsets = (
        ('Mídias do Carrossel', {
            'fields': ('medias',)
        }),
        ('Metadados', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    @admin.display(description='Quantidade de Mídias')
    def get_medias_count(self, obj):
        return obj.medias.count()

    def has_add_permission(self, request):
        return not AboutCarouselSection.objects.exists()
