from .collects.urls import urlpatterns as collects_urls
from .payments.urls import urlpatterns as payments_urls
from .users.urls import urlpatterns as users_urls

urlpatterns = users_urls + collects_urls + payments_urls
