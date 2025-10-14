import os
from datetime import timedelta
from pathlib import Path
from dotenv import load_dotenv
import dj_database_url

load_dotenv()


BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'default-secret-key')

DEBUG = os.getenv('DEBUG', False)

ALLOWED_HOSTS = [
    'api.onggabriel.com.br',
    'localhost',
    '127.0.0.1',
]

# CORS ALLOWED
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_ALL_ORIGINS = False
CORS_ALLOWED_ORIGINS = [
    os.getenv('FRONTEND_URL'),
    'https://onggabriel.com.br'
]

CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'x-csrf-token',
    'x-xsrf-token',
]

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_simplejwt',
    'drf_spectacular',
    'django_celery_results',
    'django_celery_beat',
    'corsheaders',
    'authentication',
    'customuser',
    'blog',
    'testimonial',
    'management',
    'events',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DJANGO_ENV = os.getenv('DJANGO_ENV')
if DJANGO_ENV == 'development':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'db.sqlite3'
        }
    }
else:
    DATABASES = {
        'default': dj_database_url.config(conn_max_age=600)
    }

# CUSTOM USER
AUTH_USER_MODEL = 'customuser.CustomUser'

# REST FRAMEWORK CONFIG
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'authentication.custom_jwt_cookie_auth.CustomJWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'authentication.permissions.PublicReadAndCSRFCheckPermission',
    ],
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_FILTER_BACKENDS': ['dj_rql.drf.RQLFilterBackend'],
}

# JWT CONFIGURATION
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
}

# SPECTACULAR CONFIG

SPECTACULAR_SETTINGS = {
    'TITLE': 'API Ong Gabriel',
    'DESCRIPTION': (
        'Esta é a API oficial da Ong Gabriel. '
        'Ela foi desenvolvida com Django Rest Framework para oferecer uma interface robusta e segura, '
        'permitindo o gerenciamento completo das funcionalidades da ONG. \n\n'
        'A API disponibiliza endpoint para cadastro e autenticação de usuários. \n\n'
        'Todos os endpoints seguem as melhores práticas RESTful e possuem suporte a autenticação via tokens. '
        'A documentação abaixo descreve todos os recursos disponíveis, os parâmetros esperados e exemplos de uso.'
    ),
    'VERSION': '1.0.0',
}

# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = True


STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Media Files

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# CELERY CONFIG

# CELERY_BROKER_URL = f"pyamqp://{os.getenv('RABBITMQ_DEFAULT_USER')}:{os.getenv('RABBITMQ_DEFAULT_PASS')}@rabbitmq:{os.getenv('RABBITMQ_AMQP_PORT', 5672)}//"
# CELERY_TIMEZONE = 'America/Sao_Paulo'
# CELERY_RESULT_BACKEND = 'django-db'

# JAZZMIN CONFIG

JAZZMIN_SETTINGS = {
    "site_title": "API Ong Gabriel",
    "site_header": "Ong Gabriel",
    "site_brand": "Ong Gabriel",

    "site_logo": "/images/logo.png",
    "login_logo": "/images/logo.png",
    "login_logo_dark": None,
    "site_icon": "/images/logo.png",

    "extra_css": [
        "/styles/custom.css",
    ],

    "welcome_sign": "Bem vindo(a) ao backend Ong Gabriel",
    "copyright": "Ong Gabriel",

    "show_sidebar": True,
    "navigation_expanded": True,

    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "customuser.CustomUser": "fas fa-wallet",
    },
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",

    # 'search_model': ['app.NomeModel', 'app.NomeModel',],
    'show_ui_builder': True,
}

# JAZZMIN UI THEME DEFAULT

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": False,
    "accent": "accent-primary",
    "navbar": "navbar-white navbar-light",
    "no_navbar_border": False,
    "navbar_fixed": False,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": False,
    "sidebar": "sidebar-dark-primary",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    "theme": "lux",
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-outline-primary",
        "secondary": "btn-outline-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success"
    }
}
