from rest_framework import permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from api.collects import openapi
from api.payments.serializers import PaymentInCollectSerializer
from api.utils import send_creation_email
from collects.models import Collect
from collects.tasks import deactivate_collect
from config import constants as const

from .permissions import IsAuthorOrAdminOrReadOnly
from .serializers import (CollectReadSerializer, CollectSerializer,
                          IsActiveUpdateSerializer)


@openapi.collect
class CollectViewSet(viewsets.ModelViewSet):
    """
    ViewSet для создания, чтения, редактирования и удаления
    группового сбора.
    """
    queryset = Collect.objects.all()
    http_method_names = [
        'get', 'post', 'patch', 'delete', 'head', 'options'
    ]
    permission_classes = (IsAuthorOrAdminOrReadOnly,)

    def get_serializer_class(self):
        if self.request.method in permissions.SAFE_METHODS:
            return CollectReadSerializer
        return CollectSerializer

    def perform_create(self, serializer):
        """
        Отправка письма автору о создании сбора
        и создание отложенной задачи на деактивацию сбора
        при наступлении его end_date (время окончания).
        """
        collect = serializer.save()

        subject = const.COLLECT_SUB_TEXT
        message = const.COLLECT_MESSAGE_TEXT
        send_creation_email(subject, message, collect.author.email)

        deactivate_collect.apply_async(
            args=[collect.id],
            eta=collect.end_date
        )

    def destroy(self, request, *args, **kwargs):
        """
        Переопределения метода удаления группового сбора:
        нельзя удалить сбор, если у него есть платежи.
        """
        collect = self.get_object()
        if collect.payments.exists():
            return Response(
                {'detail': 'Нельзя удалить сбор с существующими платежами.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        return super().destroy(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        """
        После создания группового сбора можно изменить
        только поле is_active.
        """
        collect = self.get_object()
        serializer = IsActiveUpdateSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

        collect.is_active = serializer.validated_data['is_active']
        collect.save()
        return Response(self.get_serializer(collect).data,
                        status=status.HTTP_200_OK)

    @openapi.payments
    @action(detail=True, methods=['get'])
    def payments(self, request, pk=None):
        """Получить все платежи к конкретному сбору."""
        collect = self.get_object()
        payments = collect.payments.all().order_by('-created_at')
        serializer = PaymentInCollectSerializer(payments, many=True)
        return Response(serializer.data)
