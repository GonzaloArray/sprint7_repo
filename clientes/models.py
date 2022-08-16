from django.db import models

# Create your models here.

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.TextField()
    customer_surname = models.TextField()
    customer_DNI = models.TextField(db_column='customer_DNI')
    customer_direccion=models.TextField(max_length=100)

    class Meta:
            db_table = 'customer'

    def __str__(self) -> str:
        return '{}'.format(self.customer_name)