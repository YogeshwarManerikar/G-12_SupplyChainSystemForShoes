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
    Price_Polyurethane = models.IntegerField(max_length=50,default=None)
    Price_Rubber = models.IntegerField(max_length=50,default=None)
    Price_Dye = models.IntegerField(max_length=50,default=None)
    Price_Packaging_Material = models.IntegerField(max_length=50,default=None)
    Price_GUM = models.IntegerField(max_length=50,default=None)
    Price_PVC_Sole = models.IntegerField(max_length=50,default=None)
    Price_TPR = models.IntegerField(max_length=50,default=None)
    Price_Hard_Thread = models.IntegerField(max_length=50,default=None)
    Price_Rexene = models.IntegerField(max_length=50,default=None)
    Price_Clips = models.IntegerField(max_length=50,default=None)
    Price_Color = models.IntegerField(max_length=50,default=None)





    product=models.ForeignKey(Product, on_delete=models.CASCADE, default=0)



    def __str__(self):
        return self.name

    class Meta:
        db_table = "RawMaterial_categories"
