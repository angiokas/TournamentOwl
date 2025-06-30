import os
from .base import *
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env.prod")
DEBUG = False

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': os.getenv('SQL_ENGINE', default='django.db.backends.sqlite3'),
        'NAME': os.getenv('SQL_DATABASE', default=os.path.join(BASE_DIR, 'db.sqlite3')),
        'USER': os.getenv('SQL_USER', default='user'),
        'PASSWORD': os.getenv('SQL_PASSWORD', default='password'),
        'HOST': os.getenv('SQL_HOST', default='localhost'),
        'PORT': os.getenv('SQL_PORT', default=''),
    }
}

SECURE_SSL_REDIRECT = True

SESSION_COOKIE_SECURE = True

CSRF_COOKIE_SECURE = True

SECURE_BROWSER_XSS_FILTER = True

