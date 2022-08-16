from django.db import models

# Create your models here.
class Cuentas(models.Model):
    account_id=models.IntegerField()
    customer_id=models.IntegerField()
    balance=models.IntegerField()
    iban=models.TextField(max_length=100)

    class Meta:
        db_table = 'cuenta'

class Empleado(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_name=models.TextField(max_length=100)
    employee_surname=models.TextField(max_length=100)
    employee_hire_date=models.TextField(max_length=300)
    employee_dni=models.TextField(max_length=100)
    branch_id=models.IntegerField()
    cd_adrress_id=models.IntegerField()

    class Meta:
        db_table = 'employeed'

class Movimientos(models.Model):
    movimiento_id = models.AutoField(primary_key=True, blank=True)
    movimientos=models.TextField(max_length=100)
    monto=models.IntegerField()
    numero_cuenta=models.IntegerField()
    tipo_operacion=models.TextField(max_length=200)
    hora=models.DateTimeField()

    class Meta:
        db_table = 'movimientos'
        verbose_name_plural = "Movimientos"

class TiposDeCuenta(models.Model):
    tipo_id = models.AutoField(primary_key=True, blank=True)
    nombre_cuenta = models.TextField()

    class Meta:
        db_table = 'account'
