from .base import *
from .base import config

DEBUG = True
#ALLOWED_HOSTS = ['localhost']
ROOT_URLCONF = 'projet_postgres.urls'


DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.postgresql_psycopg2',
        "ENGINE" :  'django.contrib.gis.db.backends.postgis',
        'NAME': config("DATABASE_NAME"),
        'USER': config("DATABASE_USER"),
        'PASSWORD': config("DATABASE_PASSWORD"),
        'HOST': config("DATABASE_HOST", "localhost"),
        'PORT': config("DATABASE_PORT"),
    }
}