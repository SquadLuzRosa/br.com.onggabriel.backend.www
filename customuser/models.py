from django.contrib.auth.models import AbstractUser
from django.db import models
from uuid import uuid4


class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False, verbose_name='ID')
    email = models.EmailField(unique=True)
    cpf = models.CharField(max_length=11, unique=True, verbose_name='CPF')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'cpf']

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        ordering = ['email', 'username']

    def __str__(self):
        return self.email
