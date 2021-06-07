from django import forms
from django.db import models

from .bata_plant import BATA_PLANT


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    user_id = models.ForeignKey(BATA_PLANT, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Plant_Product"
