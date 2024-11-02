from django.urls import path

from get_current_usd_app import views

urlpatterns = [
    path("get-current-usd/", views.get_current_usd, name="get_current_usd_route"),
]
