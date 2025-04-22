from rest_framework import mixins, permissions, viewsets
from rest_framework.permissions import AllowAny

from api.users import openapi
from users.models import User

from .serializers import UserCreationSerializer, UserSerializer


@openapi.user
class UserViewSet(
    viewsets.GenericViewSet,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
):
    '''
    ViewSet для регистрации и просмотра пользователей.
    '''
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def get_serializer_class(self):
        if self.request.method in permissions.SAFE_METHODS:
            return UserSerializer
        return UserCreationSerializer

    def perform_create(self, serializer, *args, **kwargs):
        serializer.save(*args, **kwargs)
