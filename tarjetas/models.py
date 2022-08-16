from django.db import models

# Create your models here.
class Cards(models.Model):
    cd_card_type_id=models.AutoField(primary_key=True, blank=True)
    cd_num_card=models.IntegerField()
    cd_cvv=models.IntegerField()
    cd_date_issue=models.TextField(max_length=200)
    cd_date_expiration=models.TextField(max_length=50)
    cd_card_id=models.IntegerField()
    cd_card_brand_id=models.IntegerField()
    account_id=models.IntegerField()

    class Meta:
        db_table = 'cards'