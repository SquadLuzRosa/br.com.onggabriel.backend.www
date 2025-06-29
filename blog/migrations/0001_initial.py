# Generated by Django 5.1.8 on 2025-06-11 00:05

import blog.models
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryType',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Título')),
                ('slug', models.SlugField(unique=True, verbose_name='Identificador da URL')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Descrição')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Data de atualização')),
            ],
            options={
                'verbose_name': 'Tipo de categoria',
                'verbose_name_plural': 'Tipos de categorias',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='EngagementMetrics',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True, verbose_name='ID')),
                ('views', models.IntegerField(blank=True, null=True, verbose_name='Visualizações')),
                ('shares', models.IntegerField(blank=True, null=True, verbose_name='Compartilhamento')),
                ('comments', models.IntegerField(blank=True, null=True, verbose_name='Comentários')),
                ('last_update', models.DateTimeField(auto_now=True, verbose_name='Ultima atualização')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Data de atualização')),
            ],
            options={
                'verbose_name': 'Metrica de engajamento',
                'verbose_name_plural': 'Metricas de engajamento',
                'ordering': ['views', 'shares', 'comments'],
            },
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True, verbose_name='ID')),
                ('file', models.FileField(upload_to=blog.models.upload_media, verbose_name='Arquivo')),
                ('media_type', models.CharField(choices=[('image', 'Image'), ('video', 'Video')], max_length=10, verbose_name='Tipo de arquivo')),
                ('description', models.CharField(blank=True, max_length=255, null=True, verbose_name='Descrição')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Data de atualização')),
            ],
            options={
                'verbose_name': 'Mídia do post',
                'verbose_name_plural': 'Mídias do post',
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Título')),
                ('slug', models.SlugField(unique=True, verbose_name='Identificador da URL')),
                ('summary', models.TextField(blank=True, null=True)),
                ('content', models.TextField(verbose_name='Conteudo')),
                ('status', models.CharField(choices=[('rascunho', 'Rascunho'), ('publicado', 'Publicado'), ('arquivado', 'Arquivado')], max_length=50)),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')),
                ('publication_date', models.DateTimeField(blank=True, null=True, verbose_name='Data de publicação')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Data de atualização')),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='covers/', verbose_name='Imagem da capa')),
                ('meta_keywords', models.CharField(blank=True, max_length=255, null=True, verbose_name='Palavras chaves')),
                ('meta_description', models.CharField(max_length=255, verbose_name='Meta descrição')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
                'ordering': ['title', 'status'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Título')),
                ('slug', models.SlugField(unique=True, verbose_name='Identificador da URL')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Data de atualização')),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
                'ordering': ['title'],
            },
        ),
    ]
