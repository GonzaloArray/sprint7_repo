from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name="index"),
    path('ask/', views.preguntas, name="preguntas"),
    path('turno/', views.turnosOnline, name="turnosOnline"),
]