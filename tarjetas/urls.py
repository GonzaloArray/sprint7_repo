from django.urls import path
from tarjetas import views

urlpatterns = [
    path('', views.tarjetas, name="tarjetas"),
]