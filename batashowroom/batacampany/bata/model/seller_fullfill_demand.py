from django.db import models
from .Distributor import Distributor


class Seller_fullfill_demand(models.Model):
    seller_name = models.CharField(max_length=30)
    seller_location = models.CharField(max_length=50)
    Product_name = models.CharField(max_length=100)
    Total_Demand_Quantity = models.IntegerField(max_length=100)
    Per_unit_price = models.IntegerField(max_length=100)
    Total_price = models.IntegerField(max_length=100)
    Dis_user_id =  models.ForeignKey(Distributor, on_delete=models.CASCADE)
    Dis_user_location = models.CharField(max_length=50)

    class Meta:
        db_table = "Seller_fullfill_demand"

