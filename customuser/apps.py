from django.apps import AppConfig


class CustomuserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'customuser'
    verbose_name = 'Usuários Customizado'
