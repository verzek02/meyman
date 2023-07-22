from pathlib import Path
from decouple import config
from .jazzmin import *

<<<<<<< HEAD:core/travel_app/settings/base.py
BASE_DIR = Path(__file__).resolve().parent.parent.parent
SECRET_KEY = 'django-insecure-)f(ueona)v_r-0sb)o3y!**vp)1))72xly#_motvqct3_70fq9'

DEBUG = True if config('DEBUG') == 'on' else False
=======
For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
from pathlib import Path
import os
>>>>>>> Eldiyar:core/travel_app/settings.py

ALLOWED_HOSTS = ['*']

CREATE_APPS = [
    'apps.travel',
    'apps.advertising',
]
INSTALLED_LIBRARY = [
    'django_filters',
    'jazzmin',
    'rest_framework',
    'drf_yasg'

]

DJANGO_APPS = [
     'django.contrib.admin',
     'django.contrib.auth',
     'django.contrib.contenttypes',
     'django.contrib.sessions',
     'django.contrib.messages',
     'django.contrib.staticfiles',
    ]
INSTALLED_APPS = INSTALLED_LIBRARY + CREATE_APPS + DJANGO_APPS


# JAZZMIN_SETTINGS = JAZZMIN_SETTINGS
# JAZZMIN_UI_TWEAKS = JAZZMIN_UI_TWEAKS

<<<<<<< HEAD:core/travel_app/settings/base.py
=======
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'apps.travel',
    'apps.news',
    'apps.travel_service',
]
>>>>>>> Eldiyar:core/travel_app/settings.py

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

<<<<<<< HEAD:core/travel_app/settings/base.py
SWAGGER_SETTINGS = {
    'USE_SESSION_AUTH': False,
    'SECURITY_DEFINITIONS': {
        'basic': {
            'type': 'basic'
        }
    }
}

ROOT_URLCONF = 'travel_app.urls'
=======
ROOT_URLCONF = 'core.travel_app.urls'
>>>>>>> Eldiyar:core/travel_app/settings.py

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.travel_app.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',  # Укажите путь к файлу базы данных SQLite3.
    }
}

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'
<<<<<<< HEAD:core/travel_app/settings/base.py
=======
# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field
>>>>>>> Eldiyar:core/travel_app/settings.py

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 5,
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'DEFAULT_PERMISSION_CLASSES': [
        'apps.advertising.permissions.IsAdminOrReadOnly',
    ],
}
