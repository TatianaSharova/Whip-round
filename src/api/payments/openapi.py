from http import HTTPStatus

from drf_spectacular.utils import (OpenApiExample, OpenApiResponse,
                                   extend_schema, extend_schema_view)

from .serializers import PaymentSerializer

payment = extend_schema_view(
    list=extend_schema(
        tags=['Payment'],
        summary='Получить список платежей',
        description='Возвращает список всех платежей.',
        responses={
            HTTPStatus.OK: PaymentSerializer(many=True),
        },
    ),
    retrieve=extend_schema(
        tags=['Payment'],
        summary='Получить платёж по id',
        description='Получение подробной информации о конкретном платеже.',
        responses={
            HTTPStatus.OK: PaymentSerializer,
            HTTPStatus.NOT_FOUND: OpenApiResponse(
                description='Платёж не найден',
                examples=[
                    OpenApiExample(
                        name='Платёж не найден',
                        value={'detail': 'Платёж не найден.'},
                        response_only=True,
                        status_codes=[str(HTTPStatus.NOT_FOUND)],
                    )
                ]
            ),
        },
    ),
    create=extend_schema(
        tags=['Payment'],
        summary='Создать новый платёж',
        description='Создание нового платежа для определённого сбора.',
        request=PaymentSerializer,
        responses={
            HTTPStatus.CREATED: PaymentSerializer,
            HTTPStatus.BAD_REQUEST: OpenApiResponse(
                description='Ошибка валидации или сбор не активен/завершён',
                examples=[
                    OpenApiExample(
                        name='Сбор не активен',
                        value={'non_field_errors': ['Сбор не активен.']},
                        response_only=True,
                        status_codes=[str(HTTPStatus.BAD_REQUEST)],
                    ),
                    OpenApiExample(
                        name='Сбор завершён',
                        value={'non_field_errors': ['Сбор уже завершён.']},
                        response_only=True,
                        status_codes=[str(HTTPStatus.BAD_REQUEST)],
                    ),
                ]
            ),
        },
    ),
)
