from uuid import uuid4

from django.db import models
from django.utils.text import slugify

from authentication.models import CustomUser


class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False, unique=True, verbose_name='ID')
    name = models.CharField(max_length=255, verbose_name='Nome', unique=True)
    description = models.TextField(blank=True, null=True, verbose_name='Descrição')
    views_count = models.PositiveIntegerField(default=0, verbose_name='Visualizações')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Data de atualização')

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['name']

    def __str__(self):
        return self.name.upper()

    def save(self, *args, **kwargs):
        """
        Override save to ensure category name is always lowercase.
        """
        if self.name:
            self.name = self.name.lower()
        super().save(*args, **kwargs)


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False, verbose_name='ID')
    title = models.CharField(max_length=255, verbose_name='Título')
    content = models.TextField(verbose_name='Conteúdo')
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.SET_NULL,
        null=True,
        related_name='user_author',
        verbose_name='Autor'
    )
    slug = models.SlugField(max_length=300, unique=True, editable=False)
    cover_image = models.ImageField(upload_to='posts/covers/', blank=True, null=True, verbose_name='Imagem da capa')
    meta_description = models.CharField(max_length=255, verbose_name='Meta descrição', blank=True, null=True)
    categories = models.ManyToManyField(
        Category,
        related_name='posts',
        verbose_name='Categorias'
    )

    views_count = models.PositiveIntegerField(default=0, verbose_name='Visualizações')
    shares_count = models.PositiveIntegerField(default=0, verbose_name='Compartilhamentos')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Data de atualização')

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-created_at', 'title']
        unique_together = ('author', 'title')

    def save(self, *args, **kwargs):
        if not self.slug and self.author:
            self.slug = f"{slugify(self.author.username)}/{slugify(self.title)}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title.upper()
