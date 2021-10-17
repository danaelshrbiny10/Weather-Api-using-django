from django.contrib import admin
from django.urls import path, include

import weather_api


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('weather_api.urls'))
]
