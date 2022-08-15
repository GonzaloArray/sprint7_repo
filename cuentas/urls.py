from django.urls import path
from cuentas import views

urlpatterns = [
    path('', views.cuentas, name="cuentas"),
]