from datetime import date
from decimal import Decimal
from django.db.models import F, Sum
from django.db import models
from django.utils import timezone
from future.backports.datetime import timedelta

from bata.model.bata_plant import BATA_PLANT
from bata.model.Raw_product import Raw_Product

value = (

    ('PENDING', 'PENDING'),
    ('DISPATCHED', 'DISPATCHED'),
    ('RECEIVED', 'RECEIVED'),


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
    user_id = models.ForeignKey(BATA_PLANT, on_delete=models.CASCADE, default=1)
    user_location = models.CharField(max_length=40)
    status = models.CharField(choices=value,max_length=20, default='PENDING')

    @property
    def total_price(self):
        return self.cartitem_set.aggregate(
            total_price=Sum(F('quantity') * F('Raw_type__price'))
        )['total_price'] or Decimal('0')


    class Meta:
        db_table = "RawMaterial_Demand"
