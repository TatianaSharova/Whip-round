import os

from dotenv import load_dotenv

load_dotenv()

# Django
SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = os.getenv('DEBUG_STATUS', 'False') == 'True'
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS").split()

# DB
POSTGRES_DB = os.getenv('POSTGRES_DB')
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_HOST = os.getenv('POSTGRES_HOST')
POSTGRES_PORT = os.getenv('POSTGRES_PORT')
POSTGRES_ENGINE = os.getenv('POSTGRES_ENGINE')

# Cache
CACHE_BACKEND = os.getenv('CACHE_BACKEND')
CACHE_LOCATION = os.getenv('CACHE_LOCATION')
CACHE_CLIENT_CLASS = os.getenv('CACHE_CLIENT_CLASS')

# Cacheops
CACHE_HOST = os.getenv('CACHE_HOST')
CACHE_PORT = os.getenv('CACHE_PORT')
CACHE_DB = os.getenv('CACHE_DB')

# User
USER_MAX_LENGTH = 150

# SMTP
EMAIL_BACKEND = os.getenv('EMAIL_BACKEND')
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_PORT = os.getenv('EMAIL_PORT')

# Collect
REASON_TYPES = (
    ('birthday', 'День рождения'),
    ('wedding', 'Свадьба'),
    ('charity', 'Благотворительность'),
    ('other', 'Другое'),
)
MAX_LENGTH_REASON = 20
COLLECT_MAX_LENGTH = 300
MIN_TARGET = 5
MAX_TARGET = 2_000_000_000

# Payment
MAX_PAYMENT_AMOUNT = 1_000_000_000
MIN_PAYMENT_AMOUNT = 1

# Email texts
COLLECT_SUB_TEXT = 'Ваш групповой сбор был успешно создан'
COLLECT_MESSAGE_TEXT = 'Ваш сбор был успешно создан! Начните собирать средства.'
PAYMENT_SUB_TEXT = 'Ваш платёж успешно прошел'
PAYMENT_MESSAGE_TEXT = 'Спасибо за пожертвование, ваш платёж успешно прошел!'
