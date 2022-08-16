from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from cuentas.models import Cuentas

# Create your views here.
@login_required
def cuentas(request):
    return render(request, 'cuentas.html')

@login_required
def transferencias(request):
    return render(request, 'transferencia.html')

@login_required
def prestamos(request):
    return render(request, 'prestamos.html')

@login_required
def inversiones(request):
    return render(request, 'inversiones.html')