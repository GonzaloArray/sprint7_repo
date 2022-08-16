from django.urls import path
from cuentas import views

urlpatterns = [
    path('', views.cuentas, name="cuentas"),
    path('transferencia/', views.transferencias, name="transferencias"),
    path('inversiones/', views.inversiones, name="inversiones"),
]