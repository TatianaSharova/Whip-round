from django.utils import timezone
from rest_framework import mixins, serializers, viewsets

from api.payments import openapi
from api.utils import send_creation_email
from collects.models import Payment
from config import constants as const

from .serializers import PaymentSerializer


@openapi.payment
class PaymentViewSet(
    viewsets.GenericViewSet,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
):
    """
    ViewSet для создания и просмотра платежей.
    """
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    def perform_create(self, serializer):
        """
        Проверка активности сбора перед созданием платежа.
        Если платёж прошел, то отправляем письмо автору сбора.
        """
        collect = serializer.validated_data['collect']

        if not collect.is_active:
            raise serializers.ValidationError('Сбор не активен.')
        if collect.end_date <= timezone.now():
            raise serializers.ValidationError('Сбор уже завершён.')
        serializer.save()

        subject = const.PAYMENT_SUB_TEXT
        message = const.PAYMENT_MESSAGE_TEXT
        send_creation_email(subject, message, collect.author.email)
