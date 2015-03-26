"""
Django settings for recettecuisine project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from configurations import Configuration


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATABASE_DIR = os.path.join(BASE_DIR, 'databases')


class Base(Configuration):
    """
    Basic configuration
    """
    SITE_ID = 1

    DEBUG = True
    TEMPLATE_DEBUG = True

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = 'b%s4w-g6fnj#8lqcrg%r%w5-d#m^f3^91r7ir$8&k^z2_6d55y'

    ALLOWED_HOSTS = []

    # Application definition

    INSTALLED_APPS = (
        # grappelli admin dashboard
        'grappelli',
        # default apps
        'django.contrib.sites',
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        # other apps
        'rest_framework',
        'jquery',
        'sitecuisine',
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

    TEMPLATE_CONTEXT_PROCESSORS = (
        'django.contrib.auth.context_processors.auth',
        'django.core.context_processors.debug',
        'django.core.context_processors.i18n',
        'django.core.context_processors.media',
        'django.core.context_processors.static',
        'django.core.context_processors.tz',
        'django.contrib.messages.context_processors.messages',
        'django.core.context_processors.request',
    )

    REST_FRAMEWORK = {
        # Use Django's standard `django.contrib.auth` permissions,
        # or allow read-only access for unauthenticated users.
        'DEFAULT_PERMISSION_CLASSES': [
            'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
        ]
    }

    ROOT_URLCONF = 'recettecuisine.urls'

    WSGI_APPLICATION = 'recettecuisine.wsgi.application'


    # Database
    # https://docs.djangoproject.com/en/1.7/ref/settings/#databases

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(DATABASE_DIR, 'db.sqlite3'),
        },
    }

    # Internationalization
    # https://docs.djangoproject.com/en/1.7/topics/i18n/

    LANGUAGE_CODE = 'en-us'

    TIME_ZONE = 'UTC'

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True

    # app static assets
    STATIC_URL = '/static/'

    #  general static assets
    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, "statics"),
    )

    # Logging configuration
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'verbose': {
                'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
            },
            'simple': {
                'format': '%(levelname)s %(asctime)s %(module)s %(message)s'
            },
        },
        'handlers': {
            'null': {
                'level': 'DEBUG',
                'class': 'logging.NullHandler',
            },
            'console': {
                'level': 'INFO',
                'class': 'logging.StreamHandler',
                'formatter': 'simple'
            },
            'file': {
                'level': 'WARNING',
                'class': 'logging.FileHandler',
                'filename': 'logs/recettecuisine.log',
                'formatter': 'simple'
            }
        },
        'loggers': {
            'django': {
                'handlers': ['console', 'file'],
                'level': 'WARNING',
                'propagate': False,
            },
            'django.security.*': {
                'handlers': ['console', 'file'],
                'propagate': False,
            },
            'django.request': {
                'handlers': ['file'],
                'level': 'WARNING',
                'propagate': False,
            },
            'django.request': {
                'handlers': ['file'],
                'level': 'ERROR',
                'propagate': False,
            },
            'django.db.backends': {
                'handlers': ['file'],
                'level': 'ERROR',
                'propagate': False,
            },
            'imports': {
                'handlers': ['console', 'file'],
                'level': 'INFO',
                'propagate': False,
            },
        }
    }

    # Grappelli Customization
    GRAPPELLI_ADMIN_TITLE = _('Admin')


class Prod(Base):
    # Debug configuration
    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = False
    TEMPLATE_DEBUG = False
    INTERNAL_IPS = ['*', ]
    ALLOWED_HOSTS = INTERNAL_IPS

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(DATABASE_DIR, 'db_prod.sqlite3'),
        },
    }


class Dev(Base):
    # Debug configuration
    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = True
    TEMPLATE_DEBUG = True
    INTERNAL_IPS = ['localhost', '127.0.0.1', '::1', ]
    ALLOWED_HOSTS = INTERNAL_IPS
    # Django Debug Toolbar
    INSTALLED_APPS = Base.INSTALLED_APPS + ('debug_toolbar', )
    MIDDLEWARE_CLASSES = Base.MIDDLEWARE_CLASSES + ('debug_toolbar.middleware.DebugToolbarMiddleware', )
    DEBUG_TOOLBAR_PATCH_SETTINGS = False

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(DATABASE_DIR, 'db_dev.sqlite3'),
        },
    }


class Test(Base):
    # Debug configuration
    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = True
    TEMPLATE_DEBUG = True
    INTERNAL_IPS = ['localhost', '127.0.0.1', '::1', ]
    ALLOWED_HOSTS = INTERNAL_IPS
    # Django Debug Toolbar
    INSTALLED_APPS = Base.INSTALLED_APPS + ('debug_toolbar', )
    MIDDLEWARE_CLASSES = Base.MIDDLEWARE_CLASSES + ('debug_toolbar.middleware.DebugToolbarMiddleware', )
    DEBUG_TOOLBAR_PATCH_SETTINGS = False

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(DATABASE_DIR, 'db_test.sqlite3'),
        },
    }
