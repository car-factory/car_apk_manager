from .common import *


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'car.sqlite3',
    }
}

STATIC_ROOT = "/opt/statics/"
ALLOWED_HOSTS = ["127.0.0.1:8000"]
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
