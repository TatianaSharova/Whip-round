from django.core.mail import send_mail

from config.constants import EMAIL_HOST_USER


def send_creation_email(subject, message, user_email):
    """Отправка письма пользователю о создании сбора или платежа."""
    send_mail(
        subject,
        message,
        EMAIL_HOST_USER,
        [user_email],
        fail_silently=False,
        )
