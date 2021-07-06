from django.db import models

from .bata_plant import BATA_PLANT


class Raw_Product(models.Model):
    name = models.CharField(max_length=50)
    Material_id = models.CharField(max_length=30,default='none')
    price = models.IntegerField(default=0)
    user_id = models.ForeignKey(BATA_PLANT, on_delete=models.CASCADE, default=0)
    pro
    def __str__(self):
        return self.name

    class Meta:
        db_table = "RawMaterial_Product"
