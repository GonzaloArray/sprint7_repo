from django.urls import path
from prestamos import views

urlpatterns = [
    path('', views.prestamos, name="prestamos"),
]