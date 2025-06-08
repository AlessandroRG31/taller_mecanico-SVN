from pathlib import Path
import environ

# 1) Base dir
BASE_DIR = Path(__file__).resolve().parent.parent

# 2) Cargar variables de entorno
env = environ.Env(
    DEBUG=(bool, False)
)
# lee el archivo .env en BASE_DIR
environ.Env.read_env(env_file=BASE_DIR / '.env')

# 3) Seguridad
SECRET_KEY = env('SECRET_KEY')
DEBUG = env('DEBUG')
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

# 4) Apps instaladas
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # django-autocomplete-light
    'dal',
    'dal_select2',

    # Apps del proyecto
    'mantenimiento',
    'repuestos',
    'core',
]

# 5) Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'taller_mecanico.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'taller_mecanico.wsgi.application'

# 6) Base de datos
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_HOST'),
        'PORT': env('DB_PORT', default='5432'),
    }
}

# 7) Validación de contraseñas
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# 8) Internacionalización
LANGUAGE_CODE = 'es-ES'
TIME_ZONE = 'America/El_Salvador'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# 9) Archivos estáticos
STATIC_URL = '/static/'
STATICFILES_DIRS = [ BASE_DIR / 'static' ]

# 10) Archivos multimedia
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# 11) Autenticación
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'

# 12) PK por defecto
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
