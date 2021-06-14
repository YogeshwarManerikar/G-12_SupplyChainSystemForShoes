from datetime import date, timedelta
from decimal import Decimal
from django.db.models import F, Sum
from django.db import models
from django.utils import timezone

from bata.model.seller import Seller
from bata.model.product import Product

value = (

    ('PENDING', 'PENDING'),
    ('DISPATCHED', 'DISPATCHED'),
    ('RECEIVED', 'RECEIVED'),


)
def return_date_time():
    now = timezone.now()
    return now + timedelta(days=1)


class Seller_demand(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default='None')
    Quantity = models.IntegerField(default=0)
    Demand_date = models.DateField(default=date.today)
    Requirement_date = models.DateField(default=return_date_time)
    user_id = models.ForeignKey(Seller, on_delete=models.CASCADE, default=1)
    user_location = models.CharField(max_length=40)
    status = models.CharField(choices=value,max_length=20, default='PENDING')



    class Meta:
        db_table = "Seller_demand"
