from uuid import uuid4

from django.db import models

from management.models import ManagementMedia


class Address(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False, unique=True, verbose_name='ID')

    name = models.CharField(max_length=255, verbose_name='Nome', unique=True, blank=True, null=True)
    street = models.CharField(max_length=200, verbose_name='Logradouro')
    number = models.CharField(max_length=20, verbose_name='Número', blank=True, null=True)
    district = models.CharField(max_length=100, verbose_name='Bairro', blank=True, null=True)
    city = models.CharField(max_length=100, verbose_name='Cidade')
    state = models.CharField(max_length=100, verbose_name='Estado')
    zipcode = models.CharField(max_length=8, verbose_name='CEP', blank=True, null=True)

    google_maps_url = models.URLField(max_length=500, verbose_name='URL do Google Maps', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Data de atualização')

    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'

    def __str__(self):
        base = f'{self.street}'
        if self.number:
            base += f', {self.number}'
        base += f' - {self.city}/{self.state}'
        return base


class EventType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False, unique=True, verbose_name='ID')

    name = models.CharField(max_length=255, verbose_name='Nome', unique=True)
    description = models.TextField(blank=True, null=True, verbose_name='Descrição')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Data de atualização')

    class Meta:
        verbose_name = 'Tipo de Evento'
        verbose_name_plural = 'Tipos de Evento'
        ordering = ['name']

    def __str__(self):
        return self.name.upper()

    def save(self, *args, **kwargs):
        """
        Override save to ensure type name is always lowercase.
        """
        if self.name:
            self.name = self.name.lower()
        super().save(*args, **kwargs)


class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False, unique=True, verbose_name='ID')

    type = models.ForeignKey(EventType, on_delete=models.SET_NULL, null=True, blank=True)
    event_date = models.DateTimeField(verbose_name='Data do Evento')
    event_end_time = models.TimeField(verbose_name='Hora Do Término do Evento', null=True, blank=True)
    title = models.CharField(max_length=100, verbose_name='Titulo')
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, blank=True, related_name='events', verbose_name='Endereço Completo')
    description = models.CharField(max_length=300, verbose_name='Descrição Curta')
    content = models.TextField(blank=True, null=True, verbose_name='Conteúdo do Evento')
    medias = models.ManyToManyField(ManagementMedia, blank=True, related_name='events', verbose_name='imagens do evento')
    is_participation = models.BooleanField(verbose_name='é obrigatório participação?', default=False)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Data de atualização')

    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'
        ordering = ['title', '-event_date']

    def __str__(self):
        return self.title
