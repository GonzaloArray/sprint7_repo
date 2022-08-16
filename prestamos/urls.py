from django.urls import path
from prestamos import views

urlpatterns = [
    path('prestamos/', views.prestamos, name="prestamos"),
]