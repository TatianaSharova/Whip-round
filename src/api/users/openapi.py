from http import HTTPStatus

from drf_spectacular.utils import (OpenApiExample, OpenApiResponse,
                                   OpenApiTypes, extend_schema,
                                   extend_schema_view)

from .serializers import UserCreationSerializer, UserSerializer

user = extend_schema_view(
    list=extend_schema(
        tags=['Users'],
        summary='Просмотр списка пользователей',
        description='Получение списка зарегистрированных пользователей.',
        responses={
            HTTPStatus.OK: UserSerializer,
        },
    ),
    retrieve=extend_schema(
        tags=['Users'],
        summary='Просмотр пользователя по id',
        description='Просмотр пользователя.',
        responses={
            HTTPStatus.OK: UserSerializer,
            HTTPStatus.NOT_FOUND: OpenApiResponse(

                description='Пользователь не найден',
                response=OpenApiTypes.OBJECT,
                examples=[
                    OpenApiExample(
                        name='Пользователь не найден',
                        value={'detail': 'Пользователь не найден.'},
                        response_only=True,
                        status_codes=[str(HTTPStatus.NOT_FOUND)],
                    )
                ]
            ),
        },
    ),
    create=extend_schema(
        tags=['Users'],
        summary='Регистрация нового пользователя',
        description=('Создание нового аккаунта пользователя. '
                     'Необходимы email, пароль, имя, фамилия, '
                     'отчество (при наличии).'),
        request=UserCreationSerializer,
        responses={
            HTTPStatus.CREATED: OpenApiResponse(
                response=UserCreationSerializer,
                description='Пользователь успешно создан',
                examples=[
                    OpenApiExample(
                        name='Успешная регистрация',
                        value={
                            'email': 'user@example.com',
                            'username': 'ivan365',
                            'first_name': 'Ivan',
                            'last_name': 'Ivanov',
                            'patronymic': 'Ivanovich',
                        },
                        response_only=True,
                        status_codes=[str(HTTPStatus.CREATED)],
                    )
                ]
            ),
            HTTPStatus.BAD_REQUEST: OpenApiResponse(
                response=OpenApiTypes.OBJECT,
                description='Ошибка валидации данных',
                examples=[
                    OpenApiExample(
                        name='Поля не заполнены',
                        value={
                            'email': ['Обязательное поле.'],
                            'password': ['Обязательное поле.'],
                        },
                        response_only=True,
                        status_codes=[str(HTTPStatus.BAD_REQUEST)],
                    ),
                    OpenApiExample(
                        name='Некорректный email',
                        value={
                            'email': ['Введите правильный адрес почты.'],
                        },
                        response_only=True,
                        status_codes=[str(HTTPStatus.BAD_REQUEST)],
                    ),
                ]
            ),
        }
    )
)
