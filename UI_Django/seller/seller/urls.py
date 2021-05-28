from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .views import  bwdate_report_details, Return_the_product,seller_dash,
view_invoice,profile,Demand_for_Product,change_password,seller_logout,seller_login,

urlpatterns = [
    path('bwdate_report_details',bwdate_report_details , name='bwdate_report_details'),
    path('change_password',change_password , name='change_password'),
    path('Demand_for_Product', Demand_for_Product, name='Demand_for_Product'),
    path('profile', profile, name='profile'),
    path('Return_the_product', Return_the_product, name='Return_the_product'),
    path('seller_dash',seller_dash , name='seller_dash'),
    path('view_invoice',view_invoice , name='view_invoice'),
    
    ,
    =
    path('', seller_logout, name='seller_logout'),
    path('', seller_login, name='seller_login'),

]