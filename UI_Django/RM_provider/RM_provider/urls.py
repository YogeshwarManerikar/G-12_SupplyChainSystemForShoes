from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .views import RM_dashboard,Consignments,payment_history,Requirment_for_RowMaterial,Consignments,
profile,change_password,RM_provider_logout,RM_provider_login,

urlpatterns = [
   
    path('change_password',change_password , name='change_password'),
    path('profile', profile, name='profile'),
    path('RM_dashboard',RM_dashboard , name='RM_dashboard'),
    path('view_invoice',view_invoice , name='view_invoice'),
    
    path('Requirment_for_RowMaterial',Requirment_for_RowMaterial, name='Requirment_for_RowMaterial'),
    path('Consignments',Consignments, name='Consignments'),

    
    ,
    =
    path('', RM_provider_logout, name='RM_provider_logout'),
    path('', RM_provider_login, name='RM_provider_login'),

]