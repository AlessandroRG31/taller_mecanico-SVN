# taller_mecanico/taller_mecanico/settings.py

from pathlib import Path
import os
import environ

env = environ.Env(DEBUG=(bool, False))
environ.Env.read_env()  # lee .env

# 1) Base dir
BASE_DIR = Path(__file__).resolve().parent.parent

# 2) Seguridad
SECRET_KEY = 'django-insecure-68%89)pg4w*effl+b*0gyif&gwu*vh7r2p50zfk-($)%99*g%b'
DEBUG = True
ALLOWED_HOSTS = []

# 3) Apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mantenimiento',
    'repuestos',
    'core',
]

# 4) Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 5) URLs & WSGI
ROOT_URLCONF = 'taller_mecanico.urls'
WSGI_APPLICATION = 'taller_mecanico.wsgi.application'

# 6) Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

# 7) Base de datos (PostgreSQL)
DATABASES = {
    'default': {
        'ENGINE':   'django.db.backends.postgresql',
        'NAME':     env('POSTGRES_DB'),
        'USER':     env('POSTGRES_USER'),
        'PASSWORD': env('POSTGRES_PASSWORD'),
        'HOST':     env('POSTGRES_HOST'),
        'PORT':     env('POSTGRES_PORT'),
    }
}
# 8) Validación de contraseñas
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# 9) Internacionalización
LANGUAGE_CODE = 'es-ES'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# 10) Archivos estáticos
STATIC_URL = '/static/'
STATICFILES_DIRS = [ BASE_DIR / "static" ]  # para tu carpeta global /static/
# (Los static de cada app se sirven gracias a APP_DIRS=True)

# 11) Archivos multimedia
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# 12) Autenticación
LOGIN_URL = '/login/'      # <-- IMPORTANTE: redirige a tu login_view
LOGIN_REDIRECT_URL = '/'   # después de login exitoso, a home

# 13) PK por defecto
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
