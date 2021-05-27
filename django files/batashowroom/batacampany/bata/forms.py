from django import forms

from .model.product import Product
from .model.bata_plant import BATA_PLANT
from .model.Raw_demand import Raw_Demand
from .model.Raw_product import Raw_Product


class Plant_login(forms.ModelForm):
    class Meta:
        model = BATA_PLANT
        fields = "__all__"


class Add_product(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

class editproduct(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name' ,'price']

class editrawproduct(forms.ModelForm):
    class Meta:
        model = Raw_Product
        fields = ['name','Material_id', 'price']

class RawDemand(forms.ModelForm):
    class Meta:
        model = Raw_Demand
        fields = "__all__"


class Add_rawmaterial(forms.ModelForm):
    class Meta:
        model = Raw_Product
        fields = "__all__"