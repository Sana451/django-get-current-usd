from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("get_current_usd_app.urls")),
    path('admin/', admin.site.urls),
]
