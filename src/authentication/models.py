from uuid import uuid4

from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """
    Custom user model for authentication, using email as the unique identifier.
    Includes CPF, timestamps, and active status.
    """

    id = models.UUIDField(
        primary_key=True, default=uuid4, editable=False, verbose_name='ID'
    )
    email = models.EmailField(unique=True, verbose_name='EMAIL')
    cpf = models.CharField(max_length=11, unique=True, verbose_name='CPF')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True, verbose_name='Active')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'cpf']

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        ordering = ['email', 'username']

    def __str__(self):
        return self.email
