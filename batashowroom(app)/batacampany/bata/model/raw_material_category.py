from django.db import models

from .Raw_product import Raw_Product
from .product import Product


class Raw_Product_category(models.Model):
    Polyurethane = models.IntegerField(max_length=50,default=None)
    Rubber = models.IntegerField(max_length=50,default=None)
    Dye = models.IntegerField(max_length=50,default=None)
    Packaging_Material = models.IntegerField(max_length=50,default=None)
    GUM = models.IntegerField(max_length=50,default=None)
    PVC_Sole = models.IntegerField(max_length=50,default=None)
    TPR = models.IntegerField(max_length=50,default=None)
    Hard_Thread = models.IntegerField(max_length=50,default=None)
    Rexene = models.IntegerField(max_length=50,default=None)
    Clips = models.IntegerField(max_length=50,default=None)
    Color = models.IntegerField(max_length=50,default=None)
    Price = models.IntegerField(max_length=50,default=None)
    product=models.ForeignKey(Product, on_delete=models.CASCADE, default=0)
    raw_product=models.ForeignKey(Raw_Product, on_delete=models.CASCADE, default=0)



    def __str__(self):
        return self.name

    class Meta:
        db_table = "RawMaterial_categories"
