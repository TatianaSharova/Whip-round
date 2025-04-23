import os

from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = os.getenv('DEBUG_STATUS', 'False') == 'True'
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS").split()

USER_MAX_LENGTH = 150

EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_PORT = os.getenv('EMAIL_PORT')

REASON_TYPES = (
    ('birthday', 'День рождения'),
    ('wedding', 'Свадьба'),
    ('charity', 'Благотворительность'),
    ('other', 'Другое'),
)
MAX_LENGTH_REASON = 20
COLLECT_MAX_LENGTH = 300

MAX_PAYMENT_AMOUNT = 100000000000
MIN_PAYMENT_AMOUNT = 1

COLLECT_SUB_TEXT = 'Ваш групповой сбор был успешно создан'
COLLECT_MESSAGE_TEXT = 'Ваш сбор был успешно создан! Начните собирать средства.'
PAYMENT_SUB_TEXT = 'Ваш платёж успешно прошел'
PAYMENT_MESSAGE_TEXT = 'Спасибо за пожертвование, ваш платёж успешно прошел!'
