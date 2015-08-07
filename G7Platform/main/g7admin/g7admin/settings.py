"""
Django settings for g7admin project.

Generated by 'django-admin startproject' using Django 1.8.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""
import os
from os import path
import sys

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(path.join(BASE_DIR,"../../../"))

from G7Platform.profile.settings.G7Settings import dbname,dbuser,dbhost,dbpassword,static_path,media_path,template_path

SECRET_KEY = '!-zyjvn0ev1csa165++iue^d-yo#+_02b7x2_=^08(y1-&%g&-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "Account",
    "Application",
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'g7admin.urls'

WSGI_APPLICATION = 'g7admin.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': dbname,
		'USER': dbuser,
        'PASSWORD': dbpassword,
        'HOST': dbhost,
        'PORT': '3306',
    }
}

AUTH_USER_MODEL = 'Account.G7User'


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = static_path

MEDIA_URL = '/media/'

MEDIA_ROOT = media_path

TEMPLATE_DIRS = (
    template_path,
)