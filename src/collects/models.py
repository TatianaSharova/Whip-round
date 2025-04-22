from django.db import models

from config.constants import REASON_TYPES
from users.models import User


class Collect(models.Model):
    """
    Модель группового сбора.
    """
    title = models.CharField('Название', max_length=300)
    description = models.TextField('Описание', max_length=300)
    reason = models.CharField('Повод', choices=REASON_TYPES)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    end_date = models.DateTimeField('Дата завершения сбора',
                                    null=True, blank=True)
    target = models.PositiveIntegerField(
        'Цель сбора', null=True, blank=True,
        help_text='Оставьте пустым для бесконечного сбора'
    )
    collected_amount = models.PositiveIntegerField('Собранная сумма',
                                                   default=0)
    image = models.ImageField('Обложка', upload_to='collects/',
                              null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='collects',
                               verbose_name='Автор')
    is_active = models.BooleanField('Активность', default=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.title


class Payment(models.Model):
    """
    Модель платежа.
    """
    collect = models.ForeignKey(Collect, on_delete=models.CASCADE,
                                related_name='payments',
                                verbose_name='Групповой сбор')
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='payments',
                               verbose_name='Автор')
    amount = models.PositiveIntegerField('Пожертвование')
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return f'{self.author.get_full_name()} пожертвовал(а) {self.amount}'
