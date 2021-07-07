import datetime
from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404

from .forms import Add_product, RawDemand, Add_rawmaterial, editproduct, editrawproduct, Sellerdemand, RawdemandStatus, \
    Fullfill_demandseller, tracking, sellerdemandStatus, SANDAL, HUSHPUPPIES, FORMAL, BUCKLED, BUDAPESTER, LACEUP
from .model import Raw_Demand, Product, Raw_Product, Distributor, Seller_demand
from .model.Demand_forward import Seller_fullfill_demand
from .model.Quality_check import Quality_checking
from .model.RM_provider import RM_provider
from .model.bata_plant import BATA_PLANT
from .model.seller import Seller
from .model.tracking_system import Tracking_reports


def plant_dash(request):
    if request.session.has_key('plantuid') & request.session.has_key('plantuname'):
        user = request.session.get('plantuid')

        sql = "SELECT seller_demand.id,seller_demand.Requirement_date ,name,Quantity," \
              "seller_demand.Quantity*plant_product.price as " \
              "sales FROM seller_demand, plant_product where plant_product.id = seller_demand.product_id GROUP BY " \
              "seller_demand.Requirement_date "
        posts = Seller_demand.objects.raw(sql)[:50]
        sql1 = "SELECT rd.id,rd.Requirement_date ,name,Quantity,rd.Quantity*rmp.price as Expenses FROM " \
               "rawmaterial_demand as rd, rawmaterial_product as rmp where rmp.id= rd.Raw_type_id GROUP BY " \
               "rd.Requirement_date "
        posts1 = Seller_demand.objects.raw(sql1)[:50]

        SANDAL = "SELECT id,SUM(Quantity) AS Quantity,MONTHNAME(Requirement_date) as month FROM seller_demand WHERE " \
                 "seller_demand.product_id=13 GROUP BY MONTHNAME(Requirement_date) ORDER BY `month` DESC "
        cat1 = Seller_demand.objects.raw(SANDAL)[:50]

        HUSH = "SELECT id,SUM(Quantity) AS Quantity,MONTHNAME(Requirement_date) as month FROM seller_demand WHERE " \
               "seller_demand.product_id=14 GROUP BY MONTHNAME(Requirement_date) ORDER BY `month` DESC "
        cat2 = Seller_demand.objects.raw(HUSH)[:50]

        BUCKLED = "SELECT id,SUM(Quantity) AS Quantity,MONTHNAME(Requirement_date) as month FROM seller_demand WHERE " \
                  "seller_demand.product_id=16 GROUP BY MONTHNAME(Requirement_date) ORDER BY `month` DESC "
        cat3 = Seller_demand.objects.raw(BUCKLED)[:50]

        LACEUP = "SELECT id,SUM(Quantity) AS Quantity,MONTHNAME(Requirement_date) as month FROM seller_demand WHERE " \
                 "seller_demand.product_id=17 GROUP BY MONTHNAME(Requirement_date) ORDER BY `month` DESC "
        cat4 = Seller_demand.objects.raw(LACEUP)[:50]

        BUDAPESTER = "SELECT id,SUM(Quantity) AS Quantity,MONTHNAME(Requirement_date) as month FROM seller_demand WHERE " \
                     "seller_demand.product_id=18 GROUP BY MONTHNAME(Requirement_date) ORDER BY `month` DESC "
        cat5 = Seller_demand.objects.raw(BUDAPESTER)[:50]

        return render(request, 'bata/Dashboard/assets/plantadmin/index.html',
                      {'user': request.session["plantuname"], 'id': user, 'detail': posts, 'details': posts1,
                       'sandal': cat1, 'HUSH': cat2, 'BUCKLED': cat3, 'LACEUP': cat4, 'BUDAPESTER': cat5})
    else:
        return redirect('plant_login')


def seller_dash(request):
    if request.session.has_key('selleruid') & request.session.has_key('selleruname'):
        user = request.session.get('selleruid')
        print("location haii..................")
        return render(request, 'bata/Dashboard/assets/seller/dashboard.html',
                      {'user': request.session["selleruname"], 'id': user})
    else:
        return redirect('Seller_login')


def Distributor_dash(request):
    if request.session.has_key('Distributoruid') & request.session.has_key('Distributoruname'):
        user = request.session.get('Distributorlocation')
        print(user)
        print("location haii..................")

        sql = "SELECT plant_product.id ,name,Quantity FROM seller_demand, plant_product where plant_product.id = seller_demand.product_id and seller_demand.user_id_id ='%s' GROUP BY plant_product.id " % user
        posts = Seller_demand.objects.raw(sql)[:50]
        return render(request, 'bata/Dashboard/assets/Distributor/dashboard.html',
                      {'user': request.session["Distributoruname"], 'id': user, 'details': posts})
    else:
        return redirect('Distributor_login')


def RM_dash(request):
    if request.session.has_key('rmuid') & request.session.has_key('rmuname'):
        user = request.session.get('rmuid')
        print("location haii..................")
        return render(request, 'bata/Dashboard/assets/RM_provider/dashboard.html',
                      {'user': request.session["rmuname"], 'id': user})
    else:
        return redirect('RM_provider_login')


def qc_dash(request):
    if request.session.has_key('qcuid') & request.session.has_key('qcuname'):
        user = request.session.get('qcuid')
        print("location haii..................")
        return render(request, 'bata/Dashboard/assets/Quality_check/QC_dashboard.html', {'id': user})
    else:
        return redirect('Quality_check_login')


def addcategory(request):
    return render(request, "bata/Dashboard/assets/plantadmin/add-category.html")


def stage_one_product_lot(request):
    return render(request, "bata/Dashboard/assets/plantadmin/1st-stage-productlot.html")


def stage_one_RowMaterial_lot(request):
    if request.session.has_key('plantuid') & request.session.has_key('plantuname'):
        user = request.session.get('plantuid')
        location = request.session.get('plantlocation')
    date = request.GET.get('query')

    print(date,location)
    sql = "SELECT id, SUM(Polyurethane) as poly,SUM(`Rubber`) as r,SUM(`Dye`) as d,SUM(`Packaging_Material`) as pack," \
          "SUM(`GUM`) as g,SUM(`PVC_Sole`) as pvc,SUM(`TPR`) as tpr,SUM(`Hard_Thread`) as h,SUM(`Rexene`) as re," \
          "SUM(`Clips`) as cl,SUM(`Color`) as co FROM `raw_material_demand` where raw_material_demand.status = " \
          "'DISPATCHED' and Requirement_date='%s' and user_id_id='%s' ORDER BY Requirement_date " % (date,user)
    posts = Raw_Demand.objects.raw(sql)[:10]

    return render(request, "bata/Dashboard/assets/plantadmin/1st-stage-RowMaterial-lot.html", {'detail': posts})


def addp_roduct(request):
    context = {}
    if request.session.has_key('plantuid') & request.session.has_key('plantuname'):
        user = request.session.get('plantuid')
        uname = request.session.get('plantuname')
        print(user, uname)
    # create object of form
    form = Add_product(request.POST)

    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()
        username = form.cleaned_data.get('name')
        messages.success(request, 'Product Name :  ' + username + ' Succesfully added')

        return redirect('addp_roduct')

    return render(request, "bata/Dashboard/assets/plantadmin/add-product.html",
                  {'id': request.session.get('plantuid'), 'form': form})


def add_rawmaterial_category(request):
    if request.session.has_key('plantuid') & request.session.has_key('plantuname'):
        user = request.session.get('plantuid')
        uname = request.session.get('plantuname')
        print(user, uname)
    # create object of form
    form = Add_rawmaterial(request.POST)

    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()
        messages.success(request, 'Raw Material Succesfully added')

        return redirect('add_rawmaterial_category')
    return render(request, "bata/Dashboard/assets/plantadmin/add-rawmaterial-category.html",
                  {'id': request.session.get('plantuid'), 'form': form})


def seller_demand_report(request):
    if request.session.has_key('Distributoruid') & request.session.has_key('Distributoruname'):
        user = request.session.get('Distributoruid')
        uname = request.session.get('Distributoruname')
        location = request.session.get('Distributorlocation')
        print(location)
        date = request.GET.get('query')

        sql = "SELECT * FROM seller_demand AS sd INNER JOIN seller_login AS sl ON  " \
              "sl.id=sd.user_id_id INNER JOIN plant_product AS p ON sd.product_id=p.id WHERE Demand_date='%s' AND sd.user_location ='%s' " % (
              date, location)
        posts = Seller_demand.objects.raw(sql)[:50]

        # check if form data is valid
        form = tracking(request.POST)
        if form.is_valid():
            # save the form data to model
            form.save()
            messages.success(request, 'Status updated')

        return render(request, "bata/Dashboard/assets/Distributor/seller_demand.html",
                      {'details': posts, 'form': form, 'detail': posts})


def bwdate_report_ds(request):
    return render(request, "bata/Dashboard/assets/plantadmin/bwdate-report-ds.html")


def change_password(request):
    return render(request, "bata/Dashboard/assets/plantadmin/change-password.html")


def Demand_for_Rowmaterial(request):
    if request.session.has_key('plantuid') & request.session.has_key('plantuname'):
        user = request.session.get('plantuid')
        uname = request.session.get('plantuname')
        print(user, uname)
    # create object of form
    form = RawDemand(request.POST)

    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()
        messages.success(request, 'Your Demand for the Raw material is Successfully saved.')

        return redirect('Demand_for_Rowmaterial')
    print(form)
    return render(request, "bata/Dashboard/assets/plantadmin/Demand-for-Rowmaterial.html",
                  {'id': request.session.get('plantuid'), 'location': request.session.get('plantlocation'),
                   'form': form})


def Seller_demand_product(request):
    if request.session.has_key('selleruid') & request.session.has_key('selleruname'):
        user = request.session.get('selleruid')
        sql = "SELECT * FROM seller_demand where seller_demand.user_id_id ='%s' " % user
        posts = Seller_demand.objects.raw(sql)[:50]

        print(request.session.get('sellerlocation'))
        # create object of form
        form = Sellerdemand(request.POST)
        form1 = tracking(request.POST)
        # check if form data is valid
        if form.is_valid() and form1.is_valid():
            # save the form data to model
            form.save()
            form1.save()
            messages.success(request, 'your demand was recorded successfully ')

            return redirect('Seller_demand_product')
        context = {'id': request.session.get('selleruid'), 'location': request.session.get('sellerlocation'),
                   'form': form,
                   'form1': form1, 'details': posts}
        return render(request, "bata/Dashboard/assets/seller/Demand_for_Product.html", context)


def edit_category(request):
    return render(request, "bata/Dashboard/assets/plantadmin/edit-category.html")


def edit_product(request, pk):
    if request.session.has_key('plantuid') & request.session.has_key('plantuname'):
        user = request.session.get('plantuid')
        uname = request.session.get('plantuname')
        print(user, uname)
        # create object of form
    product = Product.objects.get(id=pk)
    form = editproduct(instance=product)
    # check if form data is valid
    if request.method == 'POST':
        form = editproduct(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('manage_product')

    context = {'form': form,
               }
    return render(request, 'bata/Dashboard/assets/plantadmin/edit-product.html', context)


def manage_product(request):
    if request.session.has_key('plantuid') & request.session.has_key('plantuname'):
        user = request.session.get('plantuid')
        uname = request.session.get('plantuname')
        print(user, uname)
    sql = "SELECT * FROM plant_product where plant_product.user_id_id ='%s' " % user
    posts = Product.objects.raw(sql)[:50]

    return render(request, "bata/Dashboard/assets/plantadmin/Manage_product.html", {'detail': posts})


def edit_Rowmaterial_categories(request, pk):
    if request.session.has_key('plantuid') & request.session.has_key('plantuname'):
        user = request.session.get('plantuid')
        uname = request.session.get('plantuname')
        print(user, uname)
        # create object of form
    product = Raw_Product.objects.get(id=pk)
    form = editrawproduct(instance=product)
    # check if form data is valid
    if request.method == 'POST':
        form = editrawproduct(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('manage_Rowmaterial_categories')

    context = {'form': form,
               }
    return render(request, 'bata/Dashboard/assets/plantadmin/edit-Rowmaterial-categories.html', context)


def manage_Rowmaterial_categories(request):
    if request.session.has_key('plantuid') & request.session.has_key('plantuname'):
        user = request.session.get('plantuid')
        uname = request.session.get('plantuname')
        print(user, uname)
    sql = "SELECT * FROM rawmaterial_product where rawmaterial_product.user_id_id ='%s' " % user
    posts = Raw_Product.objects.raw(sql)[:50]

    return render(request, "bata/Dashboard/assets/plantadmin/manage-Rowmaterial-categories .html", {'detail': posts})


def productlot_status(request):
    return render(request, "bata/Dashboard/assets/plantadmin/productlot-status.html")


def productlot_status_update(request):
    return render(request, "bata/Dashboard/assets/plantadmin/productlot-status-update.html")


def profile(request):
    return render(request, "bata/Dashboard/assets/plantadmin/profile.html")


def returnproduct(request):
    return render(request, "bata/Dashboard/assets/Distributor/returnproduct.html")


def Rowmaterial_Payment(request):
    if request.session.has_key('plantuid') & request.session.has_key('plantuname'):
        location = request.session.get('plantlocation')
    sql1 = "SELECT * FROM rawmaterial_demand where rawmaterial_demand.status ='PENDING' and rawmaterial_demand.user_location = '%s'" % location
    posts1 = Raw_Demand.objects.raw(sql1)[:50]

    return render(request, "bata/Dashboard/assets/plantadmin/Rowmaterial-Payment.html",
                  {'details': posts1})


def Forward_demand_plant(request):
    if request.session.has_key('Distributoruid') & request.session.has_key('Distributoruname'):
        location = request.session.get('Distributorlocation')

    date = request.GET.get('query')
    sql1 = "SELECT pp.id,name as n,SUM(Quantity) as Quantity FROM seller_demand as sd INNER JOIN plant_product as pp ON pp.id=sd.product_id WHERE sd.Requirement_date='%s' GROUP BY pp.id" % date
    posts1 = Seller_demand.objects.raw(sql1)[:50]
    form = Fullfill_demandseller(request.POST)

    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()

        return redirect('Forward_demand_plant')

    context = {'form': form,
               'details': posts1,
               }

    return render(request, "bata/Dashboard/assets/Distributor/Forward_demand_plant.html", context)


def trackings(request):
    srh = request.GET.get('query')
    if srh is None:
        srh = 0

    print(srh)
    track = Tracking_reports.objects.filter(tracking_id__icontains=srh)

    if track.count() == 0 and srh != 0:
        messages.warning(request, "No search results found. Please refine your query.")

    return render(request, 'bata/tracking.html', {'track': track})


def Fullfill_seller_demand(request, pk):
    if request.session.has_key('Distributoruid') & request.session.has_key('Distributoruname'):
        location = request.session.get('Distributorlocation')
    sql1 = "SELECT sd.id,pp.id,SUM(sd.Quantity)as total_quantity From seller_demand AS sd INNER JOIN plant_product AS pp ON " \
           "sd.id=pp.id GROUP BY pp.id "
    posts1 = Seller_demand.objects.raw(sql1)[:50]
    product = Seller_demand.objects.get(id=pk)
    form = Fullfill_demandseller(instance=product)
    # check if form data is valid
    if request.method == 'POST':
        form = Fullfill_demandseller(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('Fullfill_seller_demand')

    context = {'form': form,
               'details': posts1,
               }
    return render(request, 'bata/Dashboard/assets/Distributor/Fullfill_seller_demand.html', context)


def RowMaterial_payment_status_update(request):
    return render(request, "bata/Dashboard/assets/plantadmin/RowMaterial-payment-status-update.html")


def Rowmaterial_Payment(request):
    return render(request, "bata/Dashboard/assets/plantadmin/Rowmaterial_Payment.html")


def sales_report_details(request):
    return render(request, "bata/Dashboard/assets/Distributor/sales-report-details.html")


def sales_report_ds(request):
    return render(request, "bata/Dashboard/assets/plantadmin/sales-report-ds.html")


def Plant_login(request):
    if request.method == "POST":
        form = BATA_PLANT.objects.filter(email=request.POST.get("email"), password=request.POST.get("password"))
        user = BATA_PLANT.get_user_by_email(request.POST.get("email"))

        print(form)
        if form.count() > 0:
            request.session["plantuname"] = user.first_name
            request.session["plantuid"] = user.id
            request.session["plantlocation"] = user.location
            return redirect('plant_dash')
        else:
            error_message = 'Email or Password invalid !!'
            return render(request, "bata/Login/Plant_admin.html", {'error': error_message})

    else:
        return render(request, "bata/Login/Plant_admin.html")


def plant_logout(request):
    request.session.clear()
    return redirect('plant_login')


def Seller_login(request):
    if request.method == "POST":
        form = Seller.objects.filter(email=request.POST.get("email"), password=request.POST.get("password"))
        user = Seller.get_user_by_email(request.POST.get("email"))

        print(form)
        if form.count() > 0:
            request.session["selleruname"] = user.first_name
            request.session["selleruid"] = user.id
            request.session["sellerlocation"] = user.location

            print(user.location)
            return redirect('seller_dash')
        else:
            error_message = 'Email or Password invalid !!'
            return render(request, "bata/Login/Seller.html", {'error': error_message})

    else:
        return render(request, "bata/Login/Seller.html")


def Seller_logout(request):
    request.session.clear()
    return redirect('Seller_login')


def Distributor_login(request):
    if request.method == "POST":
        form = Distributor.objects.filter(email=request.POST.get("email"), password=request.POST.get("password"))
        user = Distributor.get_user_by_email(request.POST.get("email"))

        print(form)
        if form.count() > 0:
            request.session["Distributoruname"] = user.first_name
            request.session["Distributoruid"] = user.id
            request.session["Distributorlocation"] = user.location

            return redirect('Distributor_dash')
        else:
            error_message = 'Email or Password invalid !!'
            return render(request, "bata/Login/Distributer.html", {'error': error_message})

    else:
        return render(request, "bata/Login/Distributer.html")


def distributor_logout(request):
    request.session.clear()
    return redirect('Distributor_login')


def RM_provider_login(request):
    if request.method == "POST":
        form = RM_provider.objects.filter(email=request.POST.get("email"), password=request.POST.get("password"))
        user = RM_provider.get_user_by_email(request.POST.get("email"))

        print(form)
        if form.count() > 0:
            request.session["rmuname"] = user.first_name
            request.session["rmuid"] = user.id
            request.session["rmlocation"] = user.location
            request.session["rmRaw_type"] = user.Raw_type_id

            return redirect('RM_dash')
        else:
            error_message = 'Email or Password invalid !!'
            return render(request, "bata/Login/RowMaterialProvider.html", {'error': error_message})

    else:
        return render(request, "bata/Login/RowMaterialProvider.html")


def RM_provider_logout(request):
    request.session.clear()
    return redirect('RM_provider_login')


def Quality_check_login(request):
    if request.method == "POST":
        form = Quality_checking.objects.filter(email=request.POST.get("email"), password=request.POST.get("password"))
        user = Quality_checking.get_user_by_email(request.POST.get("email"))

        print(form)
        if form.count() > 0:
            request.session["qcuname"] = user.first_name
            request.session["qcuid"] = user.id
            request.session["qclocation"] = user.location

            return redirect('qc_dash')
        else:
            error_message = 'Email or Password invalid !!'
            return render(request, "bata/Login/Qulity_check.html", {'error': error_message})

    else:
        return render(request, "bata/Login/Qulity_check.html")


def Quality_check_logout(request):
    request.session.clear()
    return redirect('Quality_check_login')


def bwdate_report_details(request):
    return render(request, "bata/Dashboard/assets/seller/bwdate_report_details.html")


def change_password(request):
    return render(request, "bata/Dashboard/assets/seller/change_password.html")


def profile(request):
    return render(request, "bata/Dashboard/assets/seller/profile.html")


def view_invoice(request, pk):
    if request.session.has_key('selleruid') & request.session.has_key('selleruname'):
        user = request.session.get('selleruid')
        uname = request.session.get('selleruname')

    sql = "SELECT *,dl.first_name as distributor,sl.first_name as seller ,sl.phone as slphone ,pp.price*sd.Quantity as subtotal,(pp.price*sd.Quantity*15)/100 as tax,round(((pp.price*sd.Quantity)+((pp.price*sd.Quantity*15)/100)),2) as Total FROM seller_demand as " \
          "sd INNER JOIN distributor_login as dl ON sd.user_location=dl.location INNER JOIN seller_login as sl ON " \
          "sl.id=sd.user_id_id INNER JOIN plant_product as pp ON pp.id=sd.product_id WHERE Track_id='%s'" % pk
    posts = Raw_Demand.objects.raw(sql)[:50]

    return render(request, "bata/Dashboard/assets/seller/view-invoice.html", {'invoice': posts})


def Manage_invoice(request):
    if request.session.has_key('selleruid') & request.session.has_key('selleruname'):
        user = request.session.get('selleruid')
        uname = request.session.get('selleruname')
        print(user, uname)

    sql = "SELECT * FROM seller_demand AS sd INNER JOIN seller_login AS sl ON sl.id=sd.user_id_id  where sd.status ='DISPATCHED' "
    posts = Raw_Demand.objects.raw(sql)[:50]

    return render(request, "bata/Dashboard/assets/seller/Manage_invoice.html", {'detail': posts})


def Return_the_product(request):
    return render(request, "bata/Dashboard/assets/seller/Return_the_product.html")


def Demand_for_Product(request):
    return render(request, "bata/Dashboard/assets/seller/Demand_for_Product.html")


def Consignments(request):
    if request.session.has_key('rmuid') & request.session.has_key('rmuname'):
        user = request.session.get('rmuid')
        uname = request.session.get('rmuname')
        location = request.session.get('rmlocation')
        print(location)
        sql = "SELECT * FROM rawmaterial_demand AS rm INNER JOIN rawmaterial_product AS rp ON rp.id=rm.Raw_type_id INNER JOIN bata_plant_login AS bp ON bp.location=rm.user_location  where rm.user_location ='%s' and rm.status='pending' " % location
        posts = Seller_demand.objects.raw(sql)[:50]
        return render(request, "bata/Dashboard/assets/RM_provider/Consignments.html", {'details': posts})


def Order_history(request):
    if request.session.has_key('rmuid') & request.session.has_key('rmuname'):
        user = request.session.get('rmuid')
        uname = request.session.get('rmuname')
        location = request.session.get('rmlocation')
        print(location)
        sql = "SELECT * FROM rawmaterial_demand AS rm INNER JOIN rawmaterial_product AS rp ON rp.id=rm.Raw_type_id INNER JOIN bata_plant_login AS bp ON bp.location=rm.user_location  where rm.user_location ='%s' and rm.status='DISPATCHED' " % location
        posts = Seller_demand.objects.raw(sql)[:50]
        return render(request, "bata/Dashboard/assets/RM_provider/Order_HIstory.html", {'details': posts})


def edit_rawdemand_status(request, pk):
    product = Raw_Demand.objects.get(id=pk)
    form = RawdemandStatus(instance=product)
    # check if form data is valid
    if request.method == 'POST':
        form = RawdemandStatus(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('Consignments')

    context = {'form': form,
               }
    return render(request, 'bata/Dashboard/assets/RM_provider/ship_consignment.html', context)


def edit_sellerdemand_status(request, pk):
    product = Seller_demand.objects.get(id=pk)
    # if request is not post, initialize an empty form
    form = sellerdemandStatus(request.POST or None)
    if request.method == 'POST':
        # check if form data is valid
        form = sellerdemandStatus(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('seller_demand_report')

    return render(request, 'bata/Dashboard/assets/RM_provider/ship_consignment.html', {'form': form})


def Requirment_for_RowMaterial(request):
    if request.session.has_key('rmuid') & request.session.has_key('rmuname'):
        rawmaterial = request.session.get('rmRaw_type')
        location = request.session.get('rmlocation')

    sql = "SELECT * FROM rawmaterial_demand where rawmaterial_demand.status ='PENDING' and " \
          "rawmaterial_demand.user_location ='%s' " % location
    posts = Raw_Demand.objects.raw(sql)[:50]

    return render(request, "bata/Dashboard/assets/RM_provider/RM_Manage_order.html", {'details': posts})


def payment_history(request):
    return render(request, "bata/Dashboard/assets/RM_provider/payment_history.html")


def Productlot_pickup(request):
    if request.session.has_key('plantuid') & request.session.has_key('plantuname'):
        user = request.session.get('plantuid')
        location = request.session.get('plantlocation')
    date = request.GET.get('query')

    print(date,location)
    sql = "SELECT * FROM `raw_material_demand` where raw_material_demand.status = " \
          "'DISPATCHED' and Requirement_date='%s' and user_id_id='%s' " % (date,user)
    posts = Raw_Demand.objects.raw(sql)[:10]
    return render(request, "bata/Dashboard/assets/Distributor/Productlot_pickup.html")


def invoice_from_plant(request):
    return render(request, "bata/Dashboard/assets/Distributor/invoice_from_plant.html")


def check(request):
    return render(request, "bata/Dashboard/assets/Quality_check/check.html")


def productlot_status(request):
    return render(request, "bata/Dashboard/assets/Quality_check/productlot_status.html")


def trackings(request):
    srh = request.GET.get('query')
    if srh is None:
        srh = 0

    print(srh)
    track = Tracking_reports.objects.filter(tracking_id__icontains=srh)

    if track.count() == 0 and srh != 0:
        messages.warning(request, "No search results found. Please refine your query.")

    return render(request, 'bata/tracking.html', {'track': track})


def contact(request):
    return render(request, "bata/contact.html")


def service(request):
    return render(request, "bata/service.html")


def index(request):
    return render(request, "bata/index.html")


def customer_support(request):
    return render(request, "bata/customer_support.html")


def product(request):
    if request.session.has_key('plantuid') & request.session.has_key('plantuname'):
        user = request.session.get('plantuid')
        uname = request.session.get('plantuname')
        print(user, uname)
        # create object of form
    quantity = request.GET.get('query')

    sandal = "SELECT id,`Price_Dye`,`Price_Packaging_Material`,`Price_Polyurethane`,`Price_Rubber`, " \
             "'%s'*`Packaging_Material` as pack,'%s'*Polyurethane as poly,'%s'*Dye as d ,'%s'*Rubber as r," \
             "('%s'*`Price_Rubber`)+('%s'*`Price_Packaging_Material`)+('%s'*`Price_Polyurethane`)+('%s'*`Price_Dye`) " \
             "as price FROM `rawmaterial_categories` WHERE product_id=13" % (quantity, quantity, quantity, quantity,
                                                                             quantity, quantity, quantity, quantity)
    posts1 = Raw_Demand.objects.raw(sandal)[:50]
    hush = "SELECT id,`Price_GUM`,`Price_PVC_Sole`,`Price_TPR`,`Price_Color`,`Price_Packaging_Material`, " \
           "'%s'*`Packaging_Material` as pack,'%s'*`GUM` as g,'%s'*`PVC_Sole` as p ,'%s'*`TPR` as t,'%s'*`Color` as " \
           "c,('%s'*`Price_GUM`)+('%s'*`Price_Packaging_Material`)+('%s'*`Price_PVC_Sole`)+('%s'*`Price_TPR`)+(" \
           "'%s'*`Price_Color`) as price FROM `rawmaterial_categories` WHERE product_id=14" % (
           quantity, quantity, quantity, quantity,
           quantity, quantity, quantity, quantity, quantity, quantity)
    posts2 = Raw_Demand.objects.raw(hush)[:50]
    formal = "SELECT id,`Price_Packaging_Material`,`Price_PVC_Sole`,`Price_Hard_Thread`,`Price_Color`,`Price_Rexene`, " \
             "'%s'*`Packaging_Material` as pack,'%s'*`Hard_Thread` as H,'%s'*`PVC_Sole` as p ,'%s'*`Rexene` as R,'%s'*`Color` as " \
             "c,('%s'*`Price_Packaging_Material`)+('%s'*`Price_PVC_Sole`)+('%s'*`Price_Hard_Thread`)+('%s'*`Price_Color`)+(" \
             "'%s'*`Price_Rexene`) as price FROM `rawmaterial_categories` WHERE product_id=15" % (
             quantity, quantity, quantity, quantity,
             quantity, quantity, quantity, quantity, quantity, quantity)
    posts3 = Raw_Demand.objects.raw(formal)[:50]
    buckled = "SELECT * FROM `rawmaterial_categories` WHERE product_id=16"
    posts4 = Raw_Demand.objects.raw(buckled)[:50]
    budapester = "SELECT id,`Price_Rubber`,`Price_Packaging_Material`,`Price_PVC_Sole`,`Price_Hard_Thread`,`Price_Color`, " \
                 "'%s'*`Packaging_Material` as pack,'%s'*`Hard_Thread` as H,'%s'*`PVC_Sole` as p ,'%s'*`Rubber` as R,'%s'*`Color` as " \
                 "c,('%s'*`Price_Rubber`)+('%s'*`Price_Packaging_Material`)+('%s'*`Price_PVC_Sole`)+('%s'*`Price_Hard_Thread`)+(" \
                 "'%s'*`Price_Color`) as price FROM `rawmaterial_categories` WHERE product_id=18" % (
                 quantity, quantity, quantity, quantity,
                 quantity, quantity, quantity, quantity, quantity, quantity)
    posts5 = Raw_Demand.objects.raw(budapester)[:50]
    laceup = "SELECT id,`Price_Polyurethane`,`Price_Dye`,`Packaging_Material`,`Price_PVC_Sole`,`Price_TPR`, " \
             "'%s'*`Packaging_Material` as pack,'%s'*`Dye` as D,'%s'*`PVC_Sole` as p ,'%s'*`Polyurethane` as p ,'%s'*`TPR` as t " \
             ",('%s'*`Price_Polyurethane`)+('%s'*`Price_Dye`)+('%s'*`Packaging_Material`)+('%s'*`Price_PVC_Sole`)+(" \
             "'%s'*`Price_TPR`) as price FROM `rawmaterial_categories` WHERE product_id=17" % (
             quantity, quantity, quantity, quantity,
             quantity, quantity, quantity, quantity, quantity, quantity)
    posts6 = Raw_Demand.objects.raw(laceup)[:50]

    form1 = SANDAL(request.POST)
    form2 = HUSHPUPPIES(request.POST)
    form3 = FORMAL(request.POST)
    form4 = BUCKLED(request.POST)
    form5 = BUDAPESTER(request.POST)
    form6 = LACEUP(request.POST)

    # check if form data is valid
    if form1.is_valid():
        # save the form data to model
        form1.save()
    if form2.is_valid():
        # save the form data to model
        form2.save()
    if form3.is_valid():
        # save the form data to model
        form3.save()
    if form5.is_valid():
        # save the form data to model
        form5.save()
    if form6.is_valid():
        # save the form data to model
        form6.save()
        # username = form.cleaned_data.get('name')
        messages.success(request, 'Raw Materiral Demanded successfully ')

        return redirect('product')
    context = {'form1': form1, 'form2': form2, 'form3': form3, 'form5': form5, 'form6': form6, 'posts1': posts1,
               'posts2': posts2, 'posts3': posts3, 'posts5': posts5, 'posts6': posts6, }
    return render(request, "bata/Dashboard/assets/plantadmin/product.html", context)
