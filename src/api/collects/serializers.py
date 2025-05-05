import base64
import datetime as dt

from django.core.files.base import ContentFile
from django.utils import timezone
from rest_framework import serializers

from api.payments.serializers import PaymentInCollectSerializer
from api.users.serializers import UserInCollectSerializer
from collects.models import Collect


class Base64ImageField(serializers.ImageField):
    """Кодировка изображения."""
    def to_internal_value(self, data):
        if isinstance(data, str) and data.startswith('data:image'):
            format, imgstr = data.split(';base64,')
            ext = format.split('/')[-1]

            data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)

        return super().to_internal_value(data)


class CollectSerializer(serializers.ModelSerializer):
    """Serializer для создания и редактирования группового сбора."""
    image = Base64ImageField()
    author = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    end_date = serializers.DateTimeField(
        input_formats=['%d.%m.%Y', '%d.%m.%Y %H:%M']
    )

    class Meta:
        model = Collect
        fields = ('id', 'title', 'description', 'reason', 'created_at',
                  'end_date', 'collected_amount', 'target', 'image',
                  'is_active', 'author')
        read_only_fields = ('id', 'created_at', 'collected_amount')

    def validate_end_date(self, value):
        """Проверка даты завершения сбора."""
        if value < timezone.now():
            raise serializers.ValidationError(
                'Дата завершения сбора не может быть меньше текущей даты'
            )

        if isinstance(value, dt.datetime) and value.time() == dt.time(0, 0):
            value = timezone.make_aware(dt.datetime.combine(value.date(),
                                                            dt.time.max))
        return value


class CollectReadSerializer(serializers.ModelSerializer):
    """Serializer для получения данных о групповом сборе."""
    author = UserInCollectSerializer(read_only=True)
    image = Base64ImageField()
    payments = PaymentInCollectSerializer(many=True, read_only=True)

    class Meta:
        model = Collect
        fields = ('id', 'title', 'description', 'reason', 'created_at',
                  'end_date', 'collected_amount', 'target', 'image',
                  'is_active', 'author', 'payments_count', 'payments')


class IsActiveUpdateSerializer(serializers.Serializer):
    """Serializer для обновления активности сбора."""
    is_active = serializers.BooleanField()
