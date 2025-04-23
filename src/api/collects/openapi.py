from http import HTTPStatus

from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import (OpenApiExample, OpenApiResponse,
                                   extend_schema, extend_schema_view)

from api.payments.serializers import PaymentInCollectSerializer

from .serializers import (CollectReadSerializer, CollectSerializer,
                          IsActiveUpdateSerializer)

collect = collect_docs = extend_schema_view(
    list=extend_schema(
        tags=['Collect'],
        summary='Получить список групповых сборов',
        description='Возвращает список всех групповых сборов.',
        responses={HTTPStatus.OK: CollectReadSerializer(many=True)},
    ),
    retrieve=extend_schema(
        tags=['Collect'],
        summary='Получить групповой сбор по id',
        description='Получение подробной информации о конкретном сборе.',
        responses={
            HTTPStatus.OK: CollectReadSerializer,
            HTTPStatus.NOT_FOUND: OpenApiResponse(
                description='Сбор не найден',
                response=OpenApiTypes.OBJECT,
                examples=[
                    OpenApiExample(
                        name='Сбор не найден',
                        value={'detail': 'Сбор не найден.'},
                        response_only=True,
                        status_codes=[str(HTTPStatus.NOT_FOUND)],
                    )
                ]
            ),
        },
    ),
    create=extend_schema(
        tags=['Collect'],
        summary='Создать новый групповой сбор',
        description='Создание нового группового сбора.',
        request=CollectSerializer,
        responses={
            HTTPStatus.CREATED: CollectReadSerializer,
            HTTPStatus.BAD_REQUEST: OpenApiResponse(
                response=OpenApiTypes.OBJECT,
                description='Ошибка валидации данных',
                examples=[
                    OpenApiExample(
                        name='Поля не заполнены',
                        value={'title': ['Обязательное поле.']},
                        response_only=True,
                        status_codes=[str(HTTPStatus.BAD_REQUEST)],
                    )
                ]
            ),
        },
    ),
    partial_update=extend_schema(
        tags=['Collect'],
        summary='Обновить активность сбора',
        description='Можно изменить только поле "is_active".',
        request=IsActiveUpdateSerializer,
        responses={
            HTTPStatus.OK: CollectSerializer,
            HTTPStatus.BAD_REQUEST: OpenApiResponse(
                description='Можно изменять только поле "is_active"',
                examples=[
                    OpenApiExample(
                        name='Недопустимые поля',
                        value={'detail': 'Можно изменить только поле "is_active".'},
                        response_only=True,
                        status_codes=[str(HTTPStatus.BAD_REQUEST)],
                    )
                ]
            ),
        }
    ),
    destroy=extend_schema(
        tags=['Collect'],
        summary='Удалить сбор',
        description='Можно удалить только сбор без пожертвований.',
        responses={
            HTTPStatus.NO_CONTENT: OpenApiResponse(
                description='Сбор успешно удалён'
            ),
            HTTPStatus.BAD_REQUEST: OpenApiResponse(
                description='Нельзя удалить сбор с пожертвованиями',
                examples=[
                    OpenApiExample(
                        name='Есть платежи',
                        value={'detail': 'Нельзя удалить сбор с существующими пожертвованиями.'},
                        response_only=True,
                        status_codes=[str(HTTPStatus.BAD_REQUEST)],
                    )
                ]
            ),
        }
    )
)

payments = extend_schema(
    tags=['Collect'],
    summary='Получить платежи определённого сбора',
    description='Возвращает список всех платежей для конкретного сбора.',
    responses={
        HTTPStatus.OK: PaymentInCollectSerializer(many=True),
        HTTPStatus.NOT_FOUND: OpenApiResponse(
            description='Сбор не найден',
            examples=[
                OpenApiExample(
                    name='Сбор не найден',
                    value={'detail': 'Сбор не найден.'},
                    response_only=True,
                    status_codes=[str(HTTPStatus.NOT_FOUND)],
                )
            ]
        ),
    }
)
