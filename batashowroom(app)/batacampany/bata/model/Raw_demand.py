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
    Price= models.FloatField(max_length=50, default=0)
    Polyurethane = models.FloatField(max_length=50, default=0)
    Rubber = models.FloatField(max_length=50, default=0)
    Dye = models.FloatField(max_length=50, default=0)
    Packaging_Material = models.FloatField(max_length=50, default=0)
    GUM = models.FloatField(max_length=50, default=0)
    PVC_Sole = models.FloatField(max_length=50, default=0)
    TPR = models.FloatField(max_length=50, default=0)
    Hard_Thread = models.FloatField(max_length=50, default=0)
    Rexene = models.FloatField(max_length=50, default=0)
    Clips = models.FloatField(max_length=50, default=0)
    Color = models.FloatField(max_length=50, default=0)
    Demand_date = models.DateField(default=date.today)
    Requirement_date = models.DateField(default=return_date_time)
    user_id = models.ForeignKey(BATA_PLANT, on_delete=models.CASCADE)
    user_location = models.CharField(max_length=40)
    status = models.CharField(choices=value,max_length=20, default='PENDING')


    def __str__(self):
        return self.Lot_number

    class Meta:
        db_table = "Raw_Material_Demand"
