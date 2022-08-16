from multiprocessing import context
from django.shortcuts import render
from django.core.mail import send_mail


# Create your views here.

def index(request):
    return render(request, 'index.html')

def preguntas(request):
    return render(request, 'ask.html')

def turnosOnline(request):
    return render(request, 'turnosOnline.html')