#!/bin/sh

set -e

if [ "$PROCESS_TYPE" = 'worker']; then
    echo "Iniciando Celery Worker..."
    celery -A app.celery worker -l info
elif [ "$PROCESS_TYPE" = 'beat']; then
    echo "Iniciando Celery Beat..."
    celery -A app.celery beat -l info
else
    echo "Iniciando Gunicorn (Processo Web)..."
    gunicorn app.wsgi:application --bind 0.0.0.0:8000
fi