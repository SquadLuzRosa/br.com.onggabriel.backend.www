from django.db import models
import os
import hashlib


def upload_media(instance, filename):
    instance_id = instance.id
    hash_instance = hashlib.sha256(str(instance_id).encode())
    _, extension = os.path.splitext(filename)
    sanitized_filename = hash_instance.hexdigest() + extension
    return f"home_section_media/{sanitized_filename}"


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


class HomeSection(models.Model):
    intro_text = models.CharField(max_length=255, blank=True, null=True)
    description_text = models.TextField(blank=True, null=True)
    image = models.ForeignKey(
        MediaSection,
        related_name='home_section_images',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )


class MissionSection(models.Model):
    first_text = models.TextField(blank=True, null=True)
    second_text = models.TextField(blank=True, null=True)


class AgendaSection(models.Model):
    theme = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ForeignKey(
        MediaSection,
        related_name='agenda_section_image',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )


class DonationSection(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ForeignKey(
        MediaSection,
        related_name='donation_section_image',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )


class VoluntarySection(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    sub_title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ForeignKey(
        MediaSection,
        related_name='voluntary_section_image',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
