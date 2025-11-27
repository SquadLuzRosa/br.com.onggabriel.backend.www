from uuid import uuid4

from django.db import models


class Function(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False, verbose_name='ID')
    name = models.CharField(max_length=100, unique=True, verbose_name='Nome')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Data de atualização')

    class Meta:
        verbose_name = 'Função'
        verbose_name_plural = 'Funções'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.name}'


class Depoiment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False, verbose_name='ID')
    name = models.CharField(max_length=100, verbose_name='Nome')
    function = models.ForeignKey(Function, on_delete=models.PROTECT, related_name='depoiments', verbose_name='Funções')
    message = models.TextField(verbose_name='Mensagem')
    image = models.ForeignKey('management.ManagementMedia', on_delete=models.SET_NULL, null=True)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Data de atualização')

    class Meta:
        verbose_name = 'Depoimento'
        verbose_name_plural = 'Depoimentos'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.name} - {self.function}'
