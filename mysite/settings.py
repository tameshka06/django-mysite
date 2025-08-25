import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-&0^x)8o@+y$7_vg%n7h6wz2^a_5&l!6^#t=^9grk3od0wquv7"
DEBUG = False


ALLOWED_HOSTS = ["tamerlan-blog.kz", "www.tamerlan-blog.kz"]

# -------------------
# Приложения
# -------------------
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "blog",  # наше приложение
]

# -------------------
# Middleware
# -------------------
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "mysite.urls"

# -------------------
# Шаблоны
# -------------------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],  # <- путь к твоей папке templates
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


WSGI_APPLICATION = "mysite.wsgi.application"

# -------------------
# База данных (SQLite для разработки)
# -------------------
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# -------------------
# Пароли
# -------------------
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

AUTHENTICATION_BACKENDS = [
    "blog.backends.EmailOrUsernameBackend",  # наш кастомный
    "django.contrib.auth.backends.ModelBackend",  # дефолтный
]


# -------------------
# Локализация
# -------------------
LANGUAGE_CODE = "ru-ru"
TIME_ZONE = "Asia/Almaty"
USE_I18N = True
USE_TZ = True

# -------------------
# Статика
# -------------------
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [BASE_DIR / "static"]

# -------------------
# Медиа файлы
# -------------------
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# -------------------
# Авторизация
# -------------------
LOGIN_REDIRECT_URL = "post_list"  # куда редиректить после входа
LOGOUT_REDIRECT_URL = "/"

# -------------------
# Default primary key field type
# -------------------
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# -------------------
# Email (для подтверждения аккаунтов)
# -------------------
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "sapybek.2008.tamerlan@gmail.com"
EMAIL_HOST_PASSWORD = "ST06_2008$$$"
