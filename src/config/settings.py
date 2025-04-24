from datetime import timedelta
from pathlib import Path

import config.constants as const

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = const.SECRET_KEY

DEBUG = const.DEBUG

ALLOWED_HOSTS = const.ALLOWED_HOSTS


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'djoser',
    'drf_spectacular',
    'cacheops',
    'api',
    'users',
    'collects',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

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

WSGI_APPLICATION = 'config.wsgi.application'


# Database

DATABASES = {
    'default': {
        'ENGINE': const.POSTGRES_ENGINE,
        'NAME': const.POSTGRES_DB,
        'USER': const.POSTGRES_USER,
        'PASSWORD': const.POSTGRES_PASSWORD,
        'HOST': const.POSTGRES_HOST,
        'PORT': const.POSTGRES_PORT,
    }
}

# Cache

CACHES = {
    'default': {
        'BACKEND': const.CACHE_BACKEND,
        'LOCATION': const.CACHE_LOCATION,
        'OPTIONS': {
            'CLIENT_CLASS': const.CACHE_CLIENT_CLASS,
        }
    }
}

# Cacheops

CACHEOPS_REDIS = {
    'host': const.CACHE_HOST,
    'port': const.CACHE_PORT,
    'db': const.CACHE_DB,
    'socket_timeout': 3,
}

CACHEOPS = {
    'users.user': {'ops': 'all', 'timeout': 60 * 15},
    'collects.collect': {'ops': 'all', 'timeout': 60 * 15},
    'collects.payment': {'ops': 'all', 'timeout': 60 * 15},
}

CACHEOPS_DEGRADE_ON_FAILURE = True

# Celery

CELERY_BROKER_URL = const.CACHE_LOCATION

CELERY_ACCEPT_CONTENT = ['json']

CELERY_TASK_SERIALIZER = 'json'

# Password validation

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

AUTH_USER_MODEL = 'users.User'

# DRF

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.BasicAuthentication'
    ],
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
}

# Djoser

DJOSER = {
    'SERIALIZERS': {
        'user_create': 'api.serializers.UserCreationSerializer', },
    'LOGIN_FIELD': 'email',
}

AUTHENTICATION_BACKENDS = [
    'djoser.auth_backends.LoginFieldBackend',
]

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=5),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'AUTH_HEADER_TYPES': ('Bearer',)
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'Whip-round API',
    'DESCRIPTION': 'Web service for group fundraising',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False
}

# SMTP

EMAIL_BACKEND = const.EMAIL_BACKEND
EMAIL_HOST = const.EMAIL_HOST
EMAIL_PORT = const.EMAIL_PORT
EMAIL_USE_TLS = True
EMAIL_HOST_USER = const.EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = const.EMAIL_HOST_PASSWORD


# Internationalization

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_TZ = True


# Static files

STATIC_URL = '/static/'

STATIC_ROOT = BASE_DIR / 'static'

MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
