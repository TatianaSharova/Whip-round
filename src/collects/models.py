from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import Sum

from config.constants import (COLLECT_MAX_LENGTH, MAX_LENGTH_REASON,
                              MAX_PAYMENT_AMOUNT, MIN_PAYMENT_AMOUNT,
                              REASON_TYPES)
from users.models import User


class Collect(models.Model):
    """
    Модель группового сбора.
    """
    title = models.CharField('Название', max_length=COLLECT_MAX_LENGTH)
    description = models.TextField('Описание', max_length=COLLECT_MAX_LENGTH)
    reason = models.CharField('Повод', max_length=MAX_LENGTH_REASON,
                              choices=REASON_TYPES)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    end_date = models.DateTimeField('Дата завершения сбора',
                                    null=True, blank=True)
    target = models.PositiveIntegerField(
        'Цель сбора', null=True, blank=True,
        help_text='Оставьте пустым для бесконечного сбора'
    )
    image = models.ImageField('Обложка', upload_to='collects/images/',
                              null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='collects',
                               verbose_name='Автор')
    is_active = models.BooleanField('Активность', default=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.title

    @property
    def payments_count(self) -> int:
        """
        Возвращает количество проведенных платежей для сбора.
        """
        return self.payments.count()

    @property
    def collected_amount(self) -> int:
        """
        Возвращает сумму всех платежей для сбора.
        """
        return self.payments.aggregate(total=Sum('amount'))['total'] or 0


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
    amount = models.PositiveIntegerField(
        'Сумма платежа', validators=[MinValueValidator(MIN_PAYMENT_AMOUNT),
                                     MaxValueValidator(MAX_PAYMENT_AMOUNT)])
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return f'{self.author.get_full_name()} пожертвовал(а) {self.amount}'
