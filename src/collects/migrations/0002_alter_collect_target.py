# Generated by Django 5.2 on 2025-04-24 06:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collect',
            name='target',
            field=models.PositiveIntegerField(blank=True, help_text='Оставьте пустым для бесконечного сбора', null=True, validators=[django.core.validators.MinValueValidator(5)], verbose_name='Цель сбора'),
        ),
    ]
