from django.shortcuts import render, redirect
from .forms import CreateLoad
from .models import Load
from datetime import date

# Create your views here.

def prestamos(request):
    prestamo_form = CreateLoad
    if request.method == "POST":
        prestamo_form = prestamo_form(data=request.POST)
        """ dic={
            'loan_type': request.POST['loan_type'],
            'loan_date': request.POST['loan_date'],
            'loan_total': request.POST['loan_total'],
        } """

        prestamo = Load(
            loan_type=request.POST['loan_type'],
            loan_date= date.today(),
            loan_total=request.POST['loan_total'],
            customer_id=1)
        prestamo.save()

        return render(request, 'hola.html')
    return render(request, 'prestamos.html', {'form': prestamo_form})
