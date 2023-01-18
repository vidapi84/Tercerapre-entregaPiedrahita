from django.contrib import admin
from django.urls import path, include
from appestudiantes.views import inicio


urlpatterns = [
    path('', inicio, name="inicio"),
    path('admin/', admin.site.urls),
    path('plataforma/', include('appestudiantes.urls')),
]
