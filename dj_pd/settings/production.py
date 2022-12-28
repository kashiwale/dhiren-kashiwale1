import django_heroku
from pathlib import Path
import os
BASE_DIR = Path(__file__).resolve().parent.parent
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['0.0.0.0','127.0.0.1','dhiren-kashiwale.herokuapp.com']



# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': BASE_DIR / 'db.sqlite3',
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
	#'NAME': 'dj_pd',
	#'NAME': 'XXXXXXXXXXXXXX',
        #'USER': 'admin',
	#'USER': 'XXXXXXXXXXXXXXX',
	#'PASSWORD':'admin',
        #'PASSWORD': '################################################',
        #'HOST': 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        'PORT': '5432',
    }
}


