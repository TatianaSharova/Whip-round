from rest_framework import serializers

from collects.models import Collect, Payment


class PaymentSerializer(serializers.ModelSerializer):
    """Serializer для создания платежа."""
    author = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    collect = serializers.PrimaryKeyRelatedField(
        queryset=Collect.objects.all()
    )

    class Meta:
        model = Payment
        fields = ('id', 'amount', 'created_at', 'author', 'collect')
        read_only_fields = ('id', 'created_at')


class PaymentInCollectSerializer(serializers.ModelSerializer):
    """Serializer для просмотра платежей внутри сбора."""
    author = serializers.SerializerMethodField()

    class Meta:
        model = Payment
        fields = ('id', 'amount', 'created_at', 'author')

    def get_author(self, obj) -> str:
        """Получение имени автора платежа."""
        return obj.author.get_full_name()
