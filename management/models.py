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
        ('image', 'Imagem'),
        ('video', 'Vídeo'),
    )
    file = models.FileField("Arquivo", upload_to=upload_media)
    media_type = models.CharField("Tipo de Mídia", max_length=10, choices=MEDIA_TYPES)
    description = models.CharField("Descrição", max_length=255, blank=True, null=True)

    def __str__(self):
        return self.description or f"{self.get_media_type_display()} - {self.id}"

    class Meta:
        verbose_name = "Seção de Mídia"
        verbose_name_plural = "Seções de Mídia"


class HomeSection(models.Model):
    intro_text = models.CharField("Texto de Introdução", max_length=255, blank=True, null=True)
    description_text = models.TextField("Texto de Descrição", blank=True, null=True)
    image = models.ForeignKey(
        MediaSection,
        verbose_name="Imagem",
        related_name='home_section_images',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.intro_text or f"Seção Home {self.id}"

    class Meta:
        verbose_name = "Seção da Home"
        verbose_name_plural = "Seções da Home"


class MissionSection(models.Model):
    first_text = models.TextField("Primeiro Bloco de Texto", blank=True, null=True)
    second_text = models.TextField("Segundo Bloco de Texto", blank=True, null=True)

    def __str__(self):
        return f"Seção Missão {self.id}"

    class Meta:
        verbose_name = "Seção de Missão"
        verbose_name_plural = "Seções de Missão"


class AgendaSection(models.Model):
    theme = models.CharField("Tema", max_length=100, blank=True, null=True)
    description = models.TextField("Descrição", blank=True, null=True)
    image = models.ForeignKey(
        MediaSection,
        verbose_name="Imagem",
        related_name='agenda_section_image',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.theme or f"Agenda {self.id}"

    class Meta:
        verbose_name = "Seção da Agenda"
        verbose_name_plural = "Seções da Agenda"


class DonationSection(models.Model):
    title = models.CharField("Título", max_length=100, blank=True, null=True)
    description = models.TextField("Descrição", blank=True, null=True)
    image = models.ForeignKey(
        MediaSection,
        verbose_name="Imagem",
        related_name='donation_section_image',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.title or f"Doação {self.id}"

    class Meta:
        verbose_name = "Seção de Doação"
        verbose_name_plural = "Seções de Doação"


class VoluntarySection(models.Model):
    title = models.CharField("Título", max_length=100, blank=True, null=True)
    sub_title = models.CharField("Subtítulo", max_length=100, blank=True, null=True)
    description = models.TextField("Descrição", blank=True, null=True)
    image = models.ForeignKey(
        MediaSection,
        verbose_name="Imagem",
        related_name='voluntary_section_image',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.title or f"Voluntário {self.id}"

    class Meta:
        verbose_name = "Seção de Voluntariado"
        verbose_name_plural = "Seções de Voluntariado"