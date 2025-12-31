"""
Django settings for horeb_biblio project.
Production-ready configuration for Render.com
"""

from pathlib import Path
import os
import dj_database_url

# ======================
# BASE DIR
# ======================
BASE_DIR = Path(__file__).resolve().parent.parent


# ======================
# SECURITY
# ======================
SECRET_KEY = os.environ.get(
    "SECRET_KEY",
    "django-insecure-cle-de-dev-horeb-biblio"
)

DEBUG = os.environ.get("DEBUG", "False") == "True"

ALLOWED_HOSTS = ["*"]


# ======================
# APPLICATIONS
# ======================
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "library",  # Votre application
]


# ======================
# MIDDLEWARE
# ======================
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",

    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# ======================
# URLS / WSGI
# ======================
ROOT_URLCONF = "horeb_biblio.urls"

WSGI_APPLICATION = "horeb_biblio.wsgi.application"


# ======================
# TEMPLATES
# ======================
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


# ======================
# DATABASE
# ======================
DATABASES = {
    "default": dj_database_url.config(
        default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}",
        conn_max_age=600,
    )
}


# ======================
# PASSWORD VALIDATION
# ======================
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# ======================
# INTERNATIONALIZATION
# ======================
LANGUAGE_CODE = "fr-fr"

TIME_ZONE = "Africa/Douala"

USE_I18N = True
USE_TZ = True


# ======================
# STATIC FILES (CSS, JS)
# ======================
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

STATICFILES_STORAGE = (
    "whitenoise.storage.CompressedStaticFilesStorage"
)


# ======================
# MEDIA FILES
# ======================
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"


# ======================
# SECURITY (RENDER / HTTPS)
# ======================
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

CSRF_TRUSTED_ORIGINS = [
    "https://*.onrender.com",
]


# ======================
# DEFAULT PRIMARY KEY
# ======================
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
