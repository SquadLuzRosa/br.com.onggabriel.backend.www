from uuid import uuid4

from django.db import models

from utils.file_utils import depoiment_image_upload_path


class Depoiment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False, verbose_name='ID')
    name = models.CharField(max_length=100)
    function = models.CharField(max_length=100)
    description = models.TextField()
    cover_image = models.ImageField(upload_to=depoiment_image_upload_path, blank=True, null=True, verbose_name='Foto do depoimento')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Data de atualização')

    class Meta:
        verbose_name = 'Depoiment'
        verbose_name_plural = 'Depoiments'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.name} - {self.function}'
