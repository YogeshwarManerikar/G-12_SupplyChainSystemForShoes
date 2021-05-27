from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .views import plant_dash, Plant_login, addcategory, stage_one_product_lot, stage_one_RowMaterial_lot, addp_roduct, \
    add_rawmaterial_category, bwdate_report_details, bwdate_report_ds, change_password, \
    Demand_for_Rowmaterial, edit_category, edit_product, edit_Rowmaterial_categories, \
    manage_Rowmaterial_categories, productlot_status, Rowmaterial_Payment, profile, returnproduct, \
    RowMaterial_payment_status_update, sales_report_details, productlot_status_update, sales_report_ds, view_invoice, \
    manage_product, Manage_invoice, seller_dash, Seller_login, plant_logout,Seller_logout

urlpatterns = [
    path('plant_dash', plant_dash, name='plant_dash'),
    path('addcategory', addcategory, name='addcategory'),
    path('stage_one_product_lot', stage_one_product_lot, name='stage_one_product_lot'),
    path('stage_one_RowMaterial_lot', stage_one_RowMaterial_lot, name='stage_one_RowMaterial_lot'),
    path('addp_roduct', addp_roduct, name='addp_roduct'),
    path('add_rawmaterial_category', add_rawmaterial_category, name='add_rawmaterial_category'),
    path('bwdate_report_details', bwdate_report_details, name='bwdate_report_details'),
    path('bwdate_report_ds', bwdate_report_ds, name='bwdate_report_ds'),
    path('change_password', change_password, name='change_password'),
    path('Demand_for_Rowmaterial', Demand_for_Rowmaterial, name='Demand_for_Rowmaterial'),
    path('edit_category', edit_category, name='edit_category'),
    path('edit_product/<str:pk>/', edit_product, name='edit_product'),
    path('edit_Rowmaterial_categories/<str:pk>/', edit_Rowmaterial_categories, name='edit_Rowmaterial_categories'),
    path('p_logout', plant_logout, name='logout'),
    path('s_logout', Seller_logout, name='logout'),
    path('manage_Rowmaterial_categories', manage_Rowmaterial_categories, name='manage_Rowmaterial_categories'),
    path('Manage_invoice', Manage_invoice, name='Manage_invoice'),
    path('productlot_status', productlot_status, name='productlot_status'),
    path('productlot_status_update', productlot_status_update, name='productlot_status_update'),
    path('profile', profile, name='profile'),
    path('returnproduct', returnproduct, name='returnproduct'),
    path('Rowmaterial_Payment', Rowmaterial_Payment, name='Rowmaterial_Payment'),
    path('RowMaterial_payment_status_update', RowMaterial_payment_status_update,
         name='RowMaterial_payment_status_update'),
    path('sales_report_details', sales_report_details, name='sales_report_details'),
    path('sales_report_ds', sales_report_ds, name='sales_report_ds'),
    path('view_invoice', view_invoice, name='view_invoice'),
    path('manage_product', manage_product, name='manage_product'),
    path('seller_dash', seller_dash, name='seller_dash'),
    path('', Plant_login, name='plant_login'),
    path('Seller_login', Seller_login, name='Seller_login'),

]