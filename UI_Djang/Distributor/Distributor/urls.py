from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .views import  bwdate_report_details,Distributor_dash,invoice_from_plant,
view_invoice,profile,change_password,Distributor_logout,Distributor_login,

urlpatterns = [
    path('bwdate_report_details',bwdate_report_details , name='bwdate_report_details'),
    path('change_password',change_password , name='change_password'),
    path('profile', profile, name='profile'),
    path('Distributor_dash',Distributor_dash , name='Distributor_dash'),
    path('view_invoice',view_invoice , name='view_invoice'),
    path('invoice_from_plant',invoice_from_plant , name='invoice_from_plant'),
    path('Productlot_pickup',Productlot_pickup , name='Productlot_pickup'),
    
    ,
    =
    path('', Distributor_logout, name='Distributor_logout'),
    path('', Distributor_login, name='Distributor_login'),

]