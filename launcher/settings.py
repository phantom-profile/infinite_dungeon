import os
from pathlib import Path

from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


ENV_FILE = BASE_DIR / '.env'
load_dotenv(ENV_FILE)

INSTALLED_APPS = [
    'django.contrib.contenttypes',  # Required for Django ORM
    'django.contrib.auth',  # Required for Django ORM
    'django_extensions',
    'dungeons',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

if os.environ.get('APP_ENV') == 'prod':
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ['DB_NAME'],
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASSWORD'],
        'HOST': os.environ['DB_HOST'],
    }

# Select the active database based on an environment variable
DEFAULT_AUTO_FIELD = os.environ['DEFAULT_AUTO_FIELD']
