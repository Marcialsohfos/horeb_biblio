"""
Django settings for horeb_biblio project.
Production ready for Render.com
"""
from pathlib import Path
import os
import dj_database_url # Nécessaire pour Render

# Construction des chemins
BASE_DIR = Path(__file__).resolve().parent.parent

# SÉCURITÉ : Lire la clé secrète depuis les variables d'environnement (Render)
# Sinon utilise une clé par défaut pour le local
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-cle-de-dev-horeb-biblio')

# DEBUG : Doit être False en production sur Render
# On met 'Render' dans les variables d'environnement sur le dashboard Render pour passer à False
DEBUG = 'RENDER' not in os.environ

# HÔTES AUTORISÉS : On autorise tout le monde (Render génère des noms de domaine dynamiques)
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'library', # Votre application
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # INDISPENSABLE POUR RENDER (Gère le CSS)
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'horeb_biblio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [], 
        'APP_DIRS': True, # Cherche automatiquement dans library/templates
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

WSGI_APPLICATION = 'horeb_biblio.wsgi.application'

# BASE DE DONNÉES (CONFIGURATION HYBRIDE)
# En local : Utilise db.sqlite3
# Sur Render : Utilise PostgreSQL automatiquement grâce à dj_database_url
DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///' + str(BASE_DIR / 'db.sqlite3'),
        conn_max_age=600
    )
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'fr-fr'
TIME_ZONE = 'Africa/Douala'
USE_I18N = True
USE_TZ = True

# FICHIERS STATIQUES (CSS, JS, IMAGES)
STATIC_URL = 'static/'

# Dossier où Django va rassembler tous les fichiers statiques pour Render
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Moteur de stockage optimisé pour Render
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Média (Photos élèves) - Attention, sur Render Free, ceci est effacé au redémarrage
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'