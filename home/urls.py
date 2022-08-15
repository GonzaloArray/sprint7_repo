from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name="index"),
    path('tarjetas/', views.tarjetas, name="tarjetas"),
    path('ask/', views.preguntas, name="preguntas"),
    path('turno/', views.turnosOnline, name="turnosOnline"),
    path('home_banking/', views.homeBanking, name="homeBanking"),
]