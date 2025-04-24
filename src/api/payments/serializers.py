from rest_framework import serializers

from collects.models import Collect, Payment
from config.constants import MAX_PAYMENT_AMOUNT, MIN_PAYMENT_AMOUNT


class PaymentSerializer(serializers.ModelSerializer):
    """Serializer для создания платежа."""

    amount = serializers.IntegerField(min_value=MIN_PAYMENT_AMOUNT,
                                      max_value=MAX_PAYMENT_AMOUNT)
    author = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    collect = serializers.PrimaryKeyRelatedField(
        queryset=Collect.objects.all()
    )

    class Meta:
        model = Payment
        fields = ('id', 'amount', 'created_at', 'author', 'collect')
        read_only_fields = ('id', 'created_at', 'author')


class PaymentInCollectSerializer(serializers.ModelSerializer):
    """Serializer для просмотра платежей внутри сбора."""
    author = serializers.SerializerMethodField()

    class Meta:
        model = Payment
        fields = ('id', 'amount', 'created_at', 'author')

    def get_author(self, obj) -> str:
        """Получение имени автора платежа."""
        return obj.author.get_full_name()
