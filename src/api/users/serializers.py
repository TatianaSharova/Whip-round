from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from users.models import User


class UserCreationSerializer(UserCreateSerializer):
    """Serializer для создания пользователя."""
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'username',
                  'first_name', 'last_name', 'patronymic')


class UserSerializer(serializers.ModelSerializer):
    """Serializer для получения данных пользователя."""
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'patronymic',
                  'email', 'username', 'date_joined', 'last_login')


class UserInCollectSerializer(serializers.ModelSerializer):
    """
    Serializer для отображения данных пользователя
    при просмотре группового сбора.
    """
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'patronymic', 'username')
