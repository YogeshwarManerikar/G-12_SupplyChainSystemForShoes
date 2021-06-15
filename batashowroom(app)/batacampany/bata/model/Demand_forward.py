from django.db import models
from .Distributor import Distributor
from .product import Product


class Seller_fullfill_demand(models.Model):
    Product_id = models.ForeignKey(Product, on_delete=models.CASCADE,default=-1)
    Total_Demand_Quantity = models.IntegerField(max_length=100)
    Distributor_location = models.CharField(max_length=150,default=-1)

    class Meta:
        db_table = "Seller_fullfill_demand"

