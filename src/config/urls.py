from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (SpectacularAPIView, SpectacularRedocView,
                                   SpectacularSwaggerView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/swagger/',
         SpectacularSwaggerView.as_view(url_name='schema'),
         name='swagger'),
    path('schema/redoc/',
         SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
