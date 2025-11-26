import os
from uuid import uuid4

from django.db import models
from django.utils.text import slugify


def upload_media(instance, filename):
    base, ext = os.path.splitext(filename)
    base_slug = slugify(base)
    return f'management/{base_slug}-{instance.id}{ext.lower()}'


class ManagementMedia(models.Model):
    MEDIA_TYPES = (
        ('image', 'Imagem'),
        ('video', 'Vídeo'),
    )

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False, verbose_name='ID')

    file = models.FileField(upload_to=upload_media)
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPES)

    alt_text = models.CharField(
        max_length=255,
        blank=True,
        help_text='Texto alternativo para SEO e acessibilidade.',
    )

    title = models.CharField(
        max_length=255,
        blank=True,
        help_text='Título da mídia (opcional, usado em SEO).',
    )

    caption = models.CharField(max_length=255, blank=True, help_text='Legenda curta (opcional).')

    slug = models.SlugField(max_length=255, blank=True, unique=True)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Data de atualização')

    def save(self, *args, **kwargs):
        if not self.slug:
            base = self.title or self.alt_text or 'media'
            slug = slugify(base)

            original_slug = slug
            counter = 1

            while ManagementMedia.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f'{original_slug}-{counter}'
                counter += 1

            self.slug = slug

        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.file:
            storage = self.file.storage
            file_path = self.file.name

            result = super().delete(*args, **kwargs)

            try:
                if file_path and storage.exists(file_path):
                    storage.delete(file_path)
            except Exception:
                pass

            return result
        else:
            return super().delete(*args, **kwargs)

    def __str__(self):
        return self.title or self.alt_text or f'Media {self.id}'

    class Meta:
        verbose_name = 'Mídia'
        verbose_name_plural = 'Mídias'
