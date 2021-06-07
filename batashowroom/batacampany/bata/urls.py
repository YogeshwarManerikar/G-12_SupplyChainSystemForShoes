from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .views import plant_dash, Plant_login, addcategory, stage_one_product_lot, stage_one_RowMaterial_lot, addp_roduct, \
    add_rawmaterial_category, bwdate_report_details, bwdate_report_ds, change_password, \
    Demand_for_Rowmaterial, edit_category, edit_product, edit_Rowmaterial_categories, \
    manage_Rowmaterial_categories, productlot_status, Rowmaterial_Payment, profile, returnproduct, \
    RowMaterial_payment_status_update, sales_report_details, productlot_status_update, sales_report_ds, view_invoice, \
    manage_product, Manage_invoice, seller_dash, Seller_login, plant_logout, Seller_logout, Distributor_dash, \
    distributor_logout, Distributor_login, RM_provider_login, RM_provider_logout, RM_dash, Seller_demand_product, \
    Return_the_product, seller_demand_report, Requirment_for_RowMaterial, Consignments, edit_rawdemand_status, \
    invoice_from_plant, Productlot_pickup, Quality_check_logout, Quality_check_login, qc_dash

urlpatterns = [
    path('plant_dash', plant_dash, name='plant_dash'),
    path('Distributor_dash', Distributor_dash, name='Distributor_dash'),
    path('addcategory', addcategory, name='addcategory'),
    path('stage_one_product_lot', stage_one_product_lot, name='stage_one_product_lot'),
    path('stage_one_RowMaterial_lot', stage_one_RowMaterial_lot, name='stage_one_RowMaterial_lot'),
    path('addp_roduct', addp_roduct, name='addp_roduct'),
    path('add_rawmaterial_category', add_rawmaterial_category, name='add_rawmaterial_category'),
    path('seller_demand_report', seller_demand_report, name='seller_demand_report'),
    path('bwdate_report_ds', bwdate_report_ds, name='bwdate_report_ds'),
    path('change_password', change_password, name='change_password'),
    path('Demand_for_Rowmaterial', Demand_for_Rowmaterial, name='Demand_for_Rowmaterial'),
    path('Seller_demand_product', Seller_demand_product, name='Seller_demand_product'),
    path('edit_category', edit_category, name='edit_category'),
    path('edit_product/<str:pk>/', edit_product, name='edit_product'),
    path('edit_rawdemand_status/<str:pk>/', edit_rawdemand_status, name='edit_rawdemand_status'),
    path('edit_Rowmaterial_categories/<str:pk>/', edit_Rowmaterial_categories, name='edit_Rowmaterial_categories'),
    path('p_logout', plant_logout, name='p_logout'),
    path('s_logout', Seller_logout, name='s_logout'),
    path('d_logout', distributor_logout, name='d_logout'),
    path('rm_logout', RM_provider_logout, name='rm_logout'),
    path('qc_logout', Quality_check_logout, name='qc_logout'),
    path('manage_Rowmaterial_categories', manage_Rowmaterial_categories, name='manage_Rowmaterial_categories'),
    path('Manage_invoice', Manage_invoice, name='Manage_invoice'),
    path('productlot_status', productlot_status, name='productlot_status'),
    path('productlot_status_update', productlot_status_update, name='productlot_status_update'),
    path('profile', profile, name='profile'),
    path('returnproduct', returnproduct, name='returnproduct'),
    path('Rowmaterial_Payment', Rowmaterial_Payment, name='Rowmaterial_Payment'),
    path('RowMaterial_payment_status_update', RowMaterial_payment_status_update,name='RowMaterial_payment_status_update'),
    path('sales_report_details', sales_report_details, name='sales_report_details'),
    path('sales_report_ds', sales_report_ds, name='sales_report_ds'),
    path('view_invoice', view_invoice, name='view_invoice'),
    path('manage_product', manage_product, name='manage_product'),
    path('seller_dash', seller_dash, name='seller_dash'),
    path('Distributor_dash', Distributor_dash, name='Distributor_dash'),
    path('RM_dash', RM_dash, name='RM_dash'),
    path('qc_dash', qc_dash, name='qc_dash'),
    path('', Plant_login, name='plant_login'),
    path('Seller_login', Seller_login, name='Seller_login'),
    path('Distributor_login', Distributor_login, name='Distributor_login'),
    path('RM_provider_login', RM_provider_login, name='RM_provider_login'),
    path('Quality_check_login', Quality_check_login, name='Quality_check_login'),
    path('bwdate_report_details', bwdate_report_details, name='bwdate_report_details'),
    path('change_password', change_password, name='change_password'),
    path('profile', profile, name='profile'),
    path('Return_the_product', Return_the_product, name='Return_the_product'),
    path('view_invoice', view_invoice, name='view_invoice'),

    path('change_password', change_password, name='change_password'),
    path('profile', profile, name='profile'),
    path('view_invoice', view_invoice, name='view_invoice'),

    path('Requirment_for_RowMaterial', Requirment_for_RowMaterial, name='Requirment_for_RowMaterial'),
    path('Consignments', Consignments, name='Consignments'),

    path('view_invoice', view_invoice, name='view_invoice'),
    path('invoice_from_plant', invoice_from_plant, name='invoice_from_plant'),
    path('Productlot_pickup', Productlot_pickup, name='Productlot_pickup'),

]