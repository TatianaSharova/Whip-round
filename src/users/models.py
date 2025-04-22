from django.contrib.auth.models import AbstractUser
from django.db import models

from config.constants import USER_MAX_LENGTH


class User(AbstractUser):
    """
    Модель пользователя с логином по полю email.
    """
    first_name = models.CharField('Имя', max_length=USER_MAX_LENGTH)
    last_name = models.CharField('Фамилия', max_length=USER_MAX_LENGTH)
    email = models.EmailField('Почта', max_length=USER_MAX_LENGTH, unique=True)
    patronymic = models.CharField('Отчество', max_length=150, blank=True,
                                  null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username']

    class Meta:
        ordering = ('-date_joined',)

    def __str__(self):
        return self.get_full_name()

    def get_full_name(self):
        """
        Возвращает полное имя: фамилия, имя, отчество (если есть).
        """
        if self.patronymic:
            full_name = "%s %s %s" % (self.last_name, self.first_name,
                                      self.patronymic)
        else:
            full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()
