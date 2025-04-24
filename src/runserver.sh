#!/usr/bin/env sh

python manage.py migrate --noinput
python manage.py collectstatic --noinput
cp -r /app/static/. /backend_static/static/

gunicorn --bind 0.0.0.0:8000 config.wsgi --access-logfile -