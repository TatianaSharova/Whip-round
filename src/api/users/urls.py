from django.urls import include, path
from rest_framework.routers import DefaultRouter as Router

from .views import UserViewSet

router_user = Router()
router_user.register('users', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router_user.urls)),
    path('auth/', include('djoser.urls.jwt')),
]
