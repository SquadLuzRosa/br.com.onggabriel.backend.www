from django.db import models
from uuid import uuid4


class Events(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False, unique=True, verbose_name='ID')
    type = models.CharField(max_length=100, verbose_name='Tipo do Evento')
    event_date = models.DateTimeField(verbose_name='Data do Evento')
    event_end_time = models.TimeField(verbose_name='Hora Do Término do Evento', null=True, blank=True)
    title = models.CharField(max_length=100, verbose_name='Titulo')
    address = models.CharField(max_length=100, verbose_name='Endereço', null=True, blank=True)
    link = models.URLField(max_length=200, verbose_name='Link', null=True, blank=True)
    description = models.CharField(max_length=300, verbose_name='Descrição Curta')
    content = models.TextField(blank=True, null=True, verbose_name='Conteúdo do Evento')
    image = models.ImageField(upload_to='covers/', blank=True, null=True, verbose_name='imagem do evento')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'
        ordering = ['title', '-event_date']

    def __str__(self):
        return self.title
