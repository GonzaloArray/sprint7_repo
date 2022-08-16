from django import forms
import datetime

class CreateLoad(forms.Form):
    loan_type = forms.ChoiceField(label='Elija el tipo de prestamo', choices = (('Hipotecario', 'Hipotecario'),('Personal', 'Personal'), ('Prendario', 'Prendario')), required=True)
    loan_total = forms.IntegerField(label = "Elija el monto", required=True)