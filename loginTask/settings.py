# loginTask/settings.py
from pathlib import Path
import os

# Base de directorios
BASE_DIR = Path(__file__).resolve().parent.parent

# Clave secreta para la seguridad (no la compartas en producción)
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-xyz')  # Cambia esto por una clave segura

# Modo de desarrollo (No usar DEBUG = True en producción)
DEBUG = os.environ.get('DEBUG', 'True') == 'True'

# Configuración de hosts permitidos (en producción, ajusta estos valores)
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')

# Aplicaciones instaladas (instala tus apps aquí)
INSTALLED_APPS = [
    'django.contrib.admin',  # Panel de administración de Django
    'django.contrib.auth',   # Autenticación de usuarios
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tasks',                 # Tu aplicación de tareas
    'accounts',              # Tu aplicación de cuentas de usuario
]

# Middleware para procesar las peticiones HTTP
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Archivo de URL principal (el que contiene las rutas)
ROOT_URLCONF = 'loginTask.urls'

# Configuración de plantillas HTML
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Carpeta para plantillas personalizadas
        'APP_DIRS': True,  # Habilita el uso de plantillas dentro de las apps
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

# Configuración de WSGI (para producción)
WSGI_APPLICATION = 'loginTask.wsgi.application'

# Configuración de base de datos (SQLite en este caso)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Validadores de contraseñas (para asegurar contraseñas seguras)
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

# Configuración de idioma e internacionalización
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Archivos estáticos (CSS, JavaScript, imágenes)
STATIC_URL = 'static/'

# Configuración para iniciar sesión
LOGIN_URL = '/signin'

AUTH_USER_MODEL = 'accounts.CustomUser'

# Configuración de la clave primaria para los modelos
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
