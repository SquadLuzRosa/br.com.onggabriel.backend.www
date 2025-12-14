"""
WSGI config for app project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.conf import settings
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

application = get_wsgi_application()

# Wrap with WhiteNoise to serve media files in production

if not settings.DEBUG:
    from whitenoise import WhiteNoise
    application = WhiteNoise(application)
    # Serve media files
    application.add_files(settings.MEDIA_ROOT, prefix='media/')
