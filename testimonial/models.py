from django.db import models
import os
import hashlib


def upload_media(instance, filename):
    instance_id = instance.id
    hash_instance = hashlib.sha256(str(instance_id).encode())
    _, extension = os.path.splitext(filename)
    sanitized_filename = hash_instance.hexdigest() + extension
    return f"testimonial_media/{sanitized_filename}"


class MediaSection(models.Model):
    MEDIA_TYPES = (
        ('image', 'Image'),
        ('video', 'Video'),
    )
    file = models.FileField(upload_to=upload_media)
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPES)
    description = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f'{self.media_type}'


class Depoiment(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    function = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField()
    image = models.ForeignKey(
        MediaSection,
        related_name='testimonial_images',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    def __str__(self):
        return f'{self.name} - {self.function}'
