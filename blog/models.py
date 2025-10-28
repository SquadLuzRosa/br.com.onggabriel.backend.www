from django.db import models
from uuid import uuid4
from customuser.models import CustomUser
import os
import hashlib


class CategoryType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False, unique=True, verbose_name='ID')
    title = models.CharField(max_length=255, verbose_name='Título')
    description = models.TextField(blank=True, null=True, verbose_name='Descrição')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Data de atualização')

    class Meta:
        verbose_name = 'Tipo de categoria'
        verbose_name_plural = 'Tipos de categorias'
        ordering = ['title']

    def __str__(self):
        return self.title.upper()


class Tag(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False, verbose_name='ID')
    title = models.CharField(max_length=255, verbose_name='Título')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Data de atualização')

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        ordering = ['title']

    def __str__(self):
        return self.title.upper()


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False, verbose_name='ID')
    title = models.CharField(max_length=255, verbose_name='Título')
    content = models.TextField(verbose_name='Conteudo')
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.SET_NULL,
        null=True,
        related_name='user_author',
        verbose_name='Autor'
    )
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')
    update_date = models.DateTimeField(auto_now=True, verbose_name='Data de atualização')
    cover_image = models.ImageField(upload_to='covers/', blank=True, null=True, verbose_name='Imagem da capa')
    meta_description = models.CharField(max_length=255, verbose_name='Meta descrição')
    categories = models.ManyToManyField(
        CategoryType,
        related_name='posts',
        verbose_name='Categorias'
    )
    tags = models.ManyToManyField('Tag', related_name='posts')

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-creation_date', 'title']

    def __str__(self):
        return self.title.upper()


class EngagementMetrics(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, unique=True, editable=False, verbose_name='ID')
    post = models.ForeignKey(Post, related_name='post_metrics', on_delete=models.CASCADE, verbose_name='ID do post')
    views = models.IntegerField(default=0, verbose_name='Visualizações')
    shares = models.IntegerField(default=0, verbose_name='Compartilhamento')
    comments = models.IntegerField(default=0, verbose_name='Comentários')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Data de atualização')

    class Meta:
        verbose_name = 'Metrica de engajamento'
        verbose_name_plural = 'Metricas de engajamento'
        ordering = ['views', 'shares', 'comments']

    def __str__(self):
        return f'Métricas - {self.post.title}'


def upload_media(instance, filename):
    instance_id = instance.id or uuid4().hex
    hash_instance = hashlib.sha256(str(instance_id).encode())

    _, ext = os.path.splitext(filename)
    sanitized_filename = hash_instance.hexdigest() + ext
    return f"blog/{sanitized_filename}"


class Media(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False, unique=True, verbose_name='ID')
    MEDIA_TYPES = (
        ('image', 'Image'),
        ('video', 'Video'),
    )
    post = models.ForeignKey(Post, related_name='media_post', on_delete=models.CASCADE, verbose_name='ID do post')
    file = models.FileField(upload_to=upload_media, verbose_name='Arquivo')
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPES, verbose_name='Tipo de arquivo')
    description = models.CharField(max_length=255, blank=True, null=True, verbose_name='Descrição')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Data de atualização')

    class Meta:
        verbose_name = 'Mídia do post'
        verbose_name_plural = 'Mídias do post'
        ordering = ['created_at']

    def __str__(self):
        return f"{self.media_type} - {self.post.title}"
