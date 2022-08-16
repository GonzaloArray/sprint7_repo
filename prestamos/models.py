from django.db import models

# Create your models here.
class Load(models.Model):
    loan_id = models.AutoField(primary_key=True, blank=True)
    loan_type=models.TextField(max_length=200)
    loan_date=models.TextField()
    loan_total=models.IntegerField()
    customer_id=models.IntegerField()

    class Meta:
        db_table = 'load'