from uuid import uuid4

from django.core.exceptions import ValidationError
from django.db import models

from .media import ManagementMedia


class AboutHistorySection(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    main_text = models.CharField(max_length=255)
    description = models.TextField()
    card_media = models.ForeignKey(ManagementMedia, on_delete=models.SET_NULL, null=True, related_name='history_card_media')
    background_image = models.ForeignKey(ManagementMedia, on_delete=models.SET_NULL, null=True, related_name='history_background_images')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Data de atualização')

    def save(self, *args, **kwargs):
        if not self.pk and AboutHistorySection.objects.exists():
            raise ValidationError('Só é permitido um único registro na sessão de história.')
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.main_text

    class Meta:
        verbose_name = '[SOBRE] História'
        verbose_name_plural = '[SOBRE] História'


class AboutMissionSection(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    text_1 = models.TextField()
    text_2 = models.TextField()
    media = models.ForeignKey(ManagementMedia, on_delete=models.SET_NULL, null=True)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Data de atualização')

    def save(self, *args, **kwargs):
        if not self.pk and AboutMissionSection.objects.exists():
            raise ValidationError('Só é permitido um único registro na sessão de missão.')
        return super().save(*args, **kwargs)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = '[SOBRE] Missão'
        verbose_name_plural = '[SOBRE] Missão'


class AboutValueCards(models.Model):
    MODELS_LEN = 7
    CARD_CHOICES = (
        (1, 'Card 1'),
        (2, 'Card 2'),
        (3, 'Card 3'),
        (4, 'Card 4'),
        (5, 'Card 5'),
        (6, 'Card 6'),
        (7, 'Card 7'),
    )

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False, unique=True, verbose_name='ID')

    card_number = models.PositiveSmallIntegerField(choices=CARD_CHOICES, unique=True)
    text = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Data de atualização')

    def save(self, *args, **kwargs):
        if not self.pk and AboutValueCards.objects.count() >= self.MODELS_LEN:
            raise ValidationError(f'Só podem existir {self.MODELS_LEN} cards de valores.')
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f'Card {self.card_number}'

    class Meta:
        verbose_name = '[SOBRE] Valor'
        verbose_name_plural = '[SOBRE] Valores'
        ordering = ['card_number']


class AboutIdealizersSection(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    main_text = models.CharField(max_length=255)
    idealizers = models.CharField(max_length=255)
    descrption = models.TextField()
    media = models.ForeignKey(ManagementMedia, on_delete=models.SET_NULL, null=True)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Data de atualização')

    def save(self, *args, **kwargs):
        if not self.pk and AboutIdealizersSection.objects.exists():
            raise ValidationError('Só é permitido um único registro na sessão de idealizadores.')
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.main_text

    class Meta:
        verbose_name = '[SOBRE] Idealizadores'
        verbose_name_plural = '[SOBRE] Idealizadores'


class AboutCarouselSection(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    medias = models.ManyToManyField(ManagementMedia, blank=True, related_name='carousel_sections', verbose_name='Mídias do Carrossel')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Data de atualização')

    def save(self, *args, **kwargs):
        if not self.pk and AboutCarouselSection.objects.exists():
            raise ValidationError('Só é permitido um único registro na sessão de carrossel.')
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'Carrossel ({self.medias.count()} mídias)'

    class Meta:
        verbose_name = '[SOBRE] Carrossel'
        verbose_name_plural = '[SOBRE] Carrossel'
