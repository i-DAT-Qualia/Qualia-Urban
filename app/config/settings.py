"""
Django settings for urban project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'qanur7mbhetm8_f^%ruq9d-l0=ot5e34cqm97bk_j33ucxl7ag'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Application definition

INSTALLED_APPS = (
    'accounts',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'django.contrib.postgres',
    'tastypie',
    'leaflet',
    'provider',
    'provider.oauth2',
    'registration',
    'sensors',
    'documents',
    'dashboard'
)

AUTH_USER_MODEL = 'accounts.QualiaUser'

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "qualia.tools.context_processors.branding"
)

ROOT_URLCONF = 'config.urls'

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'django_app',
        'USER': 'django',
        'PASSWORD': 'd15Bb5zo67174yi',
        'HOST': '',
        'PORT': '',
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-gb'

TIME_ZONE = 'Europe/London'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LEAFLET_CONFIG = {
    'DEFAULT_CENTER': (50.3750391347,-4.13879066706),
    'DEFAULT_ZOOM': 16,
}

CACHES = {
    'default': {
        'BACKEND': 'tools.caches.LargeMemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

#Branding settings
APP_NAME = 'Qualia-Urban'
QUALIA_NAME = 'Qualia Urban'
LOGO = 'icons/logo-meta.png'
FAVICON = 'icons/artory_favicon.ico'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = '/var/www/static/'

REST_FRAMEWORK = {
    'PAGE_SIZE': 10,
    'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend',),
}

MQTT_ADDRESS = 'broker.i-dat.org'
MQTT_PORT = 80
MQTT_SOCKET_PORT = 8000
MQTT_CLIENT_ID = 'datalab-sender'

TASTYPIE_DEFAULT_FORMATS = ['json', 'xml']
