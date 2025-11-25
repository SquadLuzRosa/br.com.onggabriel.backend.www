from uuid import uuid4

from django.core.exceptions import ValidationError
from django.db import models

from testmonial.models import Depoiment
from .media import ManagementMedia


class PresentationSection(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    top_text = models.CharField(max_length=255)
    main_text = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    image = models.ForeignKey(ManagementMedia, on_delete=models.SET_NULL, null=True)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Data de atualização')

    def save(self, *args, **kwargs):
        if not self.pk and PresentationSection.objects.exists():
            raise ValidationError('Só é permitido um único registro na sessão de apresentação da página home.')
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.main_text

    class Meta:
        verbose_name = '[HOME] Apresentação'
        verbose_name_plural = '[HOME] Apresentação'


class MissionSection(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    first_text = models.CharField(max_length=255)
    second_text = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Data de atualização')

    def save(self, *args, **kwargs):
        if not self.pk and MissionSection.objects.exists():
            raise ValidationError('Só é permitido um único registro na sessão de missão da página home.')
        return super().save(*args, **kwargs)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = '[HOME] Missão'
        verbose_name_plural = '[HOME] Missão'


class DonateSection(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    main_text = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Data de atualização')

    def save(self, *args, **kwargs):
        if not self.pk and MissionSection.objects.exists():
            raise ValidationError('Só é permitido um único registro na sessão de missão da página home.')
        return super().save(*args, **kwargs)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = '[HOME] Missão'
        verbose_name_plural = '[HOME] Missão'


class StatsCard(models.Model):
    MODELS_LEN = 4
    CARD_CHOICES = (
        (1, 'Card 1'),
        (2, 'Card 2'),
        (3, 'Card 3'),
        (4, 'Card 4'),
    )

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False, unique=True, verbose_name='ID')

    card_number = models.PositiveSmallIntegerField(choices=CARD_CHOICES, unique=True)
    stats_number = models.PositiveIntegerField()
    text = models.CharField(max_length=100)
    visible = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Data de atualização')

    def save(self, *args, **kwargs):
        if not self.pk and DepoimentCard.objects.count() >= self.MODELS_LEN:
            raise ValidationError(f'Só podem existir {self.MODELS_LEN} cards de estatísticas.')
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f'Card {self.card_number}'

    class Meta:
        verbose_name = '[HOME] Estatística'
        verbose_name_plural = '[HOME] Estatísticas'
        ordering = ['card_number']


class VolunteerSection(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    first_text = models.CharField(max_length=500)
    second_text = models.CharField(max_length=500)
    image = models.ForeignKey(ManagementMedia, on_delete=models.SET_NULL, null=True)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Data de atualização')

    def save(self, *args, **kwargs):
        if not self.pk and PresentationSection.objects.exists():
            raise ValidationError('Só é permitido um único registro na sessão de voluntário da página home.')
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '[HOME] Seja um voluntário'
        verbose_name_plural = '[HOME] Seja um voluntário'


class DepoimentCard(models.Model):
    MODELS_LEN = 3
    CARD_CHOICES = (
        (1, 'Card 1'),
        (2, 'Card 2'),
        (3, 'Card 3'),
    )

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False, unique=True, verbose_name='ID')

    card_number = models.PositiveSmallIntegerField(choices=CARD_CHOICES, unique=True)
    depoiment = models.ForeignKey(Depoiment, on_delete=models.SET_NULL, blank=True, null=True)
    visible = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Data de atualização')

    def save(self, *args, **kwargs):
        if not self.pk and DepoimentCard.objects.count() >= self.MODELS_LEN:
            raise ValidationError(f'Só podem existir {self.MODELS_LEN} cards de depoimento.')
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f'Card {self.card_number}'

    class Meta:
        verbose_name = '[HOME] Depoimentos'
        verbose_name_plural = '[HOME] Depoimentos'
        ordering = ['card_number']


class ContactSection(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    instagram_url = models.URLField(blank=True, null=True)
    instagram_icon = models.BooleanField(default=False)

    whatsapp_url = models.URLField(blank=True, null=True)
    whatsapp_icon = models.BooleanField(default=False)

    twitter_url = models.URLField(blank=True, null=True)
    twitter_icon = models.BooleanField(default=False)

    facebook_url = models.URLField(blank=True, null=True)
    facebook_icon = models.BooleanField(default=False)

    youtube_url = models.URLField(blank=True, null=True)
    youtube_icon = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.pk and ContactSection.objects.exists():
            raise ValidationError("Só é permitido um único registro na sessão de contato.")
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "[HOME] Contato"
        verbose_name_plural = "[HOME] Contato"


class TributeSection(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    text = models.CharField(max_length=255)
    left_image = models.ForeignKey(ManagementMedia, on_delete=models.SET_NULL, null=True, related_name='tribute_left_images')
    right_image = models.ForeignKey(ManagementMedia, on_delete=models.SET_NULL, null=True, related_name='tribute_right_images')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Data de atualização')

    def save(self, *args, **kwargs):
        if not self.pk and PresentationSection.objects.exists():
            raise ValidationError('Só é permitido um único registro na sessão de homenagem da página home.')
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = '[HOME] Homenagem'
        verbose_name_plural = '[HOME] Homenagem'
