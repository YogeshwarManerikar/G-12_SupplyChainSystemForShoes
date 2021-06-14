from datetime import date, timedelta
from decimal import Decimal
from django.db.models import F, Sum
from django.db import models
from django.utils import timezone

from bata.model.bata_plant import BATA_PLANT
from bata.model.Raw_product import Raw_Product

value = (

    ('PENDING', 'PENDING'),
    ('DISPATCHED', 'DISPATCHED'),


)
def return_date_time():
    now = timezone.now()
    return now + timedelta(days=1)


class Raw_Demand(models.Model):
    Lot_number = models.CharField(max_length=30)
    Raw_type = models.ForeignKey(Raw_Product, on_delete=models.CASCADE, default='None')
    Quantity = models.IntegerField(default=0)
    Demand_date = models.DateField(default=date.today)
    Requirement_date = models.DateField(default=return_date_time)
    user_id = models.ForeignKey(BATA_PLANT, on_delete=models.CASCADE)
    user_location = models.CharField(max_length=40)
    status = models.CharField(choices=value,max_length=20, default='PENDING')


    def __str__(self):
        return self.Lot_number

    class Meta:
        db_table = "RawMaterial_Demand"
