from datetime import date, timedelta
from decimal import Decimal
from django.db.models import F, Sum
from django.db import models
from django.utils import timezone

from .bata_plant import BATA_PLANT
from .Quality_check import Quality_checking
from .Raw_demand import Raw_Demand


class Cheking(models.Model):

    Lot_number = models.ForeignKey(Raw_Demand, on_delete=models.CASCADE, default=0)
    ok_pcs = models.IntegerField(default=0)
    Defected_pcs = models.IntegerField(default=0)
    plant_id = models.ForeignKey(BATA_PLANT, on_delete=models.CASCADE, default=0)
    Qualitycheck_id = models.ForeignKey(Quality_checking, on_delete=models.CASCADE, default=0)


    class Meta:
        db_table = "Product_Checking"
