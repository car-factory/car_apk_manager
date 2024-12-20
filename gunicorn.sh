# WSGI module name
DJANGO_WSGI_MODULE=car_apk_manager.wsgi

# Start Django Unicorn
cd /opt/car_apk_manager
exec .py3/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
    --workers 3 \
    --bind 0.0.0.0:8000
