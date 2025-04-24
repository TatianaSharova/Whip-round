import base64
import random

from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from django.db import IntegrityError
from django.utils import timezone
from faker import Faker

from collects.models import Collect, Payment
from collects.tasks import deactivate_collect
from config import constants as const
from users.models import User

fake = Faker()


class Command(BaseCommand):
    """Генерация моковых пользователей, сборов и платежей"""

    def add_arguments(self, parser):
        parser.add_argument('--users', type=int, default=300)
        parser.add_argument('--collects', type=int, default=500)
        parser.add_argument('--payments', type=int, default=2000)

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Начинаем генерацию данных...'))

        users_list = self._create_users(**options)
        if not users_list:
            return

        collects_list = self._create_collects(users_list=users_list, **options)
        if not collects_list:
            return

        payments = self._create_payments(collects_list=collects_list,
                                         users_list=users_list, **options)

        if payments:
            self.stdout.write(self.style.SUCCESS('Создание данных успешно завершено'))

    def _create_users(self, **options):
        """Создание пользователей с уникальным именем и email."""
        try:
            users = [
                User.objects.create(
                    username=fake.unique.user_name(),
                    email=fake.unique.email(),
                    first_name=fake.first_name(),
                    last_name=fake.last_name(),
                    patronymic=fake.first_name(),
                    password='Test_password123'
                    ) for _ in range(options['users'])
            ]
        except IntegrityError:
            self.stdout.write(self.style.ERROR('Ошибка при создании пользователей'))
        finally:
            if users:
                self.stdout.write(f'Создано пользователей: {len(users)}')
        return users

    def _create_collects(self, users_list, **options):
        """
        Создание сборов и постановка задачи на деактивацию сбора
        при наступлении end_date.
        """
        try:
            collects = []
            for i in range(options['collects']):
                collect = Collect.objects.create(
                    title=fake.sentence(nb_words=4),
                    description=fake.paragraph(nb_sentences=3),
                    reason=random.choice(
                        [r[0] for r in Collect._meta.get_field('reason').choices]
                    ),
                    end_date=timezone.now() + timezone.timedelta(
                        days=random.randint(1, 30)
                    ),
                    target=random.randint(const.MIN_TARGET, const.MAX_TARGET),
                    author=random.choice(users_list),
                    image=ContentFile(base64.b64decode(
                        'R0lGODlhAQABAIAAAAAAAAAAACH5BAAAAAAALAAAAAABAAEAAAICTAEAOw=='
                    ), name=f'temp_{i}.gif')
                )

                deactivate_collect.apply_async((collect.id,), eta=collect.end_date)
                collects.append(collect)
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Ошибка при создании сборов: {e}'))
        finally:
            if collects:
                self.stdout.write(f'Создано сборов: {len(collects)}')
        return collects

    def _create_payments(self, collects_list, users_list, **options):
        """Создание платежей."""
        try:
            payments = [
                Payment.objects.create(
                    collect=random.choice(collects_list),
                    author=random.choice(users_list),
                    amount=random.randint(const.MIN_PAYMENT_AMOUNT,
                                          const.MAX_PAYMENT_AMOUNT)
                ) for _ in range(options['payments'])
            ]
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Ошибка при создании платежей: {e}'))
        finally:
            if payments:
                self.stdout.write(f'Создано платежей: {len(payments)}')
        return payments
