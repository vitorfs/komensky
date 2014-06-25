from unipath import Path
PROJECT_DIR = Path(__file__).parent

import dj_database_url

SECRET_KEY = '35j-(-!9e!e9g1jd=nv2y*4*9b0_93$+b5w@j7si(_&mi_0*ge'

DEBUG = True

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['127.0.0.1']

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'komensky.core',
    'komensky.courses',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'komensky.urls'

WSGI_APPLICATION = 'komensky.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': PROJECT_DIR.child('db.sqlite3'),
    }
}

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = PROJECT_DIR.parent.child('staticfiles')
STATICFILES_DIRS = (PROJECT_DIR.child('static'),)

MEDIA_URL = '/media/'
MEDIA_ROOT = PROJECT_DIR.parent.child('media')

TEMPLATE_DIRS = (PROJECT_DIR.child('templates'),)

LOGIN_URL = '/login/'
