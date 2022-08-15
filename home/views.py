from multiprocessing import context
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')
def tarjetas(request):
    return render(request, 'tarjetas.html')
def preguntas(request):
    return render(request, 'ask.html')
def turnosOnline(request):
    return render(request, 'turnosOnline.html')
def homeBanking(request):
    return render(request, 'homeBanking.html')