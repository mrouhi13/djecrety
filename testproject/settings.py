import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.insert(0, BASE_DIR)

SECRET_KEY = '_'

DEBUG = True

INSTALLED_APPS = [
    'djecrety',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3'
    }
}
