from django.urls import include, path
from rest_framework.routers import DefaultRouter as Router

from .views import CollectViewSet

router_collect = Router()
router_collect.register('collects', CollectViewSet, basename='collect')

urlpatterns = [
    path('', include(router_collect.urls)),
]
