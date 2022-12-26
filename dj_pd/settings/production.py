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
	'NAME': 'de7jcjpbkqene6',
        #'USER': 'admin',
	'USER': 'hfqykgfumjflsn',
	#'PASSWORD':'admin',
        'PASSWORD': '92c49618f902b3690e4250b5655e4e575f89ebadcafd7a746199f650308762bc',
        'HOST': 'ec2-3-230-122-20.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}


