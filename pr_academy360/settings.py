"""
Django settings for pr_academy360 project.

Generated by 'django-admin startproject' using Django 5.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-yvw08x6sry3!pg0)55)rgfzl5w-@8dmt-s@#0a=k=)d&!bvj^o'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost','academy360.co.za']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app_academy360',
]

WHITENOISE_MIMETYPES = {'.css': 'text/css'}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'pr_academy360.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'app_academy360/templates/home'),
                 os.path.join(BASE_DIR, 'app_academy360/templates/auth')],
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

WSGI_APPLICATION = 'pr_academy360.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases
#Local
# DATABASES = {
#      'default': {
#          'ENGINE': 'django.db.backends.postgresql',
#          'NAME': 'DB_Academy360',  # Replace with your PostgreSQL database name
#          'USER': 'root',  # Replace with your PostgreSQL username
#          'PASSWORD': 'Cyber@#War8728',  # Replace with your PostgreSQL password
#          'HOST': 'i4gogsw084okw4kgw4ww4cgw',  # Typically 'localhost' or the IP of your PostgreSQL server
#          'PORT': '5432',  # Usually 5432 for PostgreSQL
#      }
# }

#Remote
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'DB_Academy360',  # Replace with your PostgreSQL database name
        'USER': 'postgres',  # Replace with your PostgreSQL username
        'PASSWORD': 'ov3E79fqnN0AtV20r0DIALYM2XvwwGYwWqdj5iIrYhJ5c6Kgi3mdzDK5Sp2qDvIP',  # Replace with your PostgreSQL password
        'HOST': '102.211.204.58',  # Typically 'localhost' or the IP of your PostgreSQL server
        'PORT': '5432',  # Usually 5432 for PostgreSQL
    }
}
#postgres://root:Monday@01@102.211.204.58:5432/DB_Academy360
#postgres://root:Cyber@#War8728@102.211.204.58:5432/DB_Academy360
#postgres://postgres:ov3E79fqnN0AtV20r0DIALYM2XvwwGYwWqdj5iIrYhJ5c6Kgi3mdzDK5Sp2qDvIP@102.211.204.58:5432/postgres
#postgres://postgres:ov3E79fqnN0AtV20r0DIALYM2XvwwGYwWqdj5iIrYhJ5c6Kgi3mdzDK5Sp2qDvIP@vkwokco40oo004skkgo8w0w8:5432/postgres


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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

CSRF_TRUSTED_ORIGINS = ['https://academy360.co.za', 'https://localhost:8001']

# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-ZA'

TIME_ZONE = 'Africa/Johannesburg'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

LOGIN_REDIRECT_URL = '/index/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"