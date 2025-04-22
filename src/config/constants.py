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

REASON_TYPES = ('birthday', 'Birthday',
                'wedding', 'Wedding',
                'charity', 'Charity',
                'other', 'Other')
