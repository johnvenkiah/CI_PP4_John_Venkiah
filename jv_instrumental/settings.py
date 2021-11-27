"""
Django settings for jv_instrumental project.

Generated by 'django-admin startproject' using Django 3.2.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
from pathlib import Path
import dj_database_url
from django.contrib.messages import constants as messages
import boto3  # noqa
import storages  # noqa
if os.path.isfile('env.py'):
    import env  # noqa


development = os.environ.get('DEVELOPMENT')


# Build paths inside the project like this: BASE_DIR / 'subdir'.

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

if development:
    ALLOWED_HOSTS = ['localhost']
else:
    ALLOWED_HOSTS = ['instru-mental.herokuapp.com']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'django.contrib.staticfiles',
    'storages',
    'django_social_share',
    'main',
    'user_profile',
    'search',
    'ads',
    'contact',
    'user_account',
    'msg',
]

SITE_ID = 1

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'jv_instrumental.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.media',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'jv_instrumental.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

if 'USE_AWS' not in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

else:

    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': ('django.contrib.auth.'
                 'password_validation.UserAttributeSimilarityValidator'),
    },
    {
        'NAME': ('django.contrib.auth.'
                 'password_validation.MinimumLengthValidator'),
    },
    {
        'NAME': ('django.contrib.auth.'
                 'password_validation.CommonPasswordValidator'),
    },
    {
        'NAME': ('django.contrib.auth.'
                 'password_validation.NumericPasswordValidator'),
    },
]

ACCOUNT_EMAIL_VERIFICATION = 'none'


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

if 'USE_AWS' in os.environ:
    # Cache control
    AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=94608000',
    }

    # Bucket Config
    AWS_STORAGE_BUCKET_NAME = 'instru-mental-content'
    AWS_S3_REGION_NAME = 'eu-north-1'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

    # Static and media files
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'

    STATIC_ROOT = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    # Override static and media URLs in production
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/


# STATIC_URL = '/static/'
# STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# if not development:
# # STATIC_URL = '/static/'
# # STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

#     AWS_S3_OBJECT_PARAMETERS = {
#         'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
#         'CacheControl': 'max-age=94608000',
#     }

#     AWS_STORAGE_BUCKET_NAME = 'instru-mental-content'
#     AWS_S3_REGION_NAME = 'eu-north-1'
#     AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
#     AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
#     AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

#     # Static and media files
#     STATICFILES_STORAGE = 'custom_storages.StaticStorage'
#     STATICFILES_LOCATION = 'static'
#     DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
#     MEDIAFILES_LOCATION = 'media'

#     # Override static and media URLs in production
#     STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
#     MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'

# DEFAULT_FILE_STORAGE = 'main.storage_backends.MediaStorage'

# Gmail Settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get('USER_HOST_EMAIL')
EMAIL_HOST_PASSWORD = os.environ.get('USER_HOST_PASSWORD')

GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
