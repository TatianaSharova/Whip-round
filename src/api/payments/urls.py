from django.urls import include, path
from rest_framework.routers import DefaultRouter as Router

from .views import PaymentViewSet

router_payment = Router()
router_payment.register('payments', PaymentViewSet, basename='payment')

urlpatterns = [
    path('', include(router_payment.urls)),
]
