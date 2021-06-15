from django import forms

from .model.seller import Seller
from .model.product import Product
from .model.bata_plant import BATA_PLANT
from .model.Raw_demand import Raw_Demand
from .model.Raw_product import Raw_Product
from .model.seller_demand import Seller_demand
from .model.Demand_forward import Seller_fullfill_demand


class Plant_login(forms.ModelForm):
    class Meta:
        model = BATA_PLANT
        fields = "__all__"


class Sellerlogin(forms.ModelForm):
    class Meta:
        model = Seller
        fields = "__all__"


class Add_product(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"


class Fullfill_demandseller(forms.ModelForm):
    class Meta:
        model = Seller_fullfill_demand
        fields = "__all__"


class editproduct(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price']


class editrawproduct(forms.ModelForm):
    class Meta:
        model = Raw_Product
        fields = ['name', 'Material_id', 'price']


class RawdemandStatus(forms.ModelForm):
    class Meta:
        model = Raw_Demand
        fields = ['status']


class RawDemand(forms.ModelForm):
    class Meta:
        model = Raw_Demand
        fields = ['Lot_number', 'Raw_type', 'Quantity', 'Demand_date', 'Requirement_date', 'user_id', 'user_location']


class Sellerdemand(forms.ModelForm):
    class Meta:
        model = Seller_demand
        fields = ['product', 'Quantity', 'Demand_date', 'Requirement_date', 'user_id', 'user_location']


class Add_rawmaterial(forms.ModelForm):
    class Meta:
        model = Raw_Product
        fields = "__all__"
