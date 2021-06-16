from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404

from .forms import Add_product, RawDemand, Add_rawmaterial, editproduct, editrawproduct, Sellerdemand, RawdemandStatus, \
    Fullfill_demandseller, tracking
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
        return render(request, 'bata/Dashboard/assets/plantadmin/dashboard.html',
                      {'user': request.session["plantuname"], 'id': user})
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
        uname = request.session.get('plantuname')
    sql = "SELECT * FROM rawmaterial_demand where rawmaterial_demand.status = 'DISPATCHED'"
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
        sql = "SELECT * FROM seller_login AS sl INNER JOIN seller_demand AS sd ON  " \
              "sl.id=sd.user_id_id INNER JOIN plant_product AS p ON sd.product_id=p.id and sd.user_location ='%s' " % location
        posts = Seller_demand.objects.raw(sql)[:50]

        form = tracking(request.POST)

        # check if form data is valid
        if form.is_valid():
            # save the form data to model
            form.save()
            messages.success(request, 'Message has been send to seller')

    return render(request, "bata/Dashboard/assets/Distributor/seller_demand.html", {'details': posts,'form':form})


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

        return render(request, "bata/Dashboard/assets/seller/Demand_for_Product.html",
                      {'id': request.session.get('selleruid'), 'location': request.session.get('sellerlocation'),
                       'form': form, 'form1': form1, 'details': posts})


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


def view_invoice(request, pk):
    if request.session.has_key('uid') & request.session.has_key('uname'):
        user = request.session.get('uid')
        uname = request.session.get('uname')
        print(user, uname)

        context = {

        }
        return render(request, 'bata/Dashboard/assets/plantadmin/view-invoice.html', context)


def manage_Rowmaterial_categories(request):
    if request.session.has_key('plantuid') & request.session.has_key('plantuname'):
        user = request.session.get('plantuid')
        uname = request.session.get('plantuname')
        print(user, uname)
    sql = "SELECT * FROM rawmaterial_product where rawmaterial_product.user_id_id ='%s' " % user
    posts = Raw_Product.objects.raw(sql)[:50]

    return render(request, "bata/Dashboard/assets/plantadmin/manage-Rowmaterial-categories .html", {'detail': posts})


def Manage_invoice(request):
    if request.session.has_key('uid') & request.session.has_key('uname'):
        user = request.session.get('uid')
        uname = request.session.get('uname')
        print(user, uname)

    sql = "SELECT * FROM rawmaterial_demand where rawmaterial_demand.status ='DISPATCHED' and " \
          "rawmaterial_demand.user_id_id ='%s' " % user
    posts = Raw_Demand.objects.raw(sql)[:50]

    return render(request, "bata/Dashboard/assets/plantadmin/Manage_invoice.html", {'detail': posts})


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
    sql1 = "SELECT plant_product.id,name as n,SUM(Quantity) as Quantity FROM `seller_demand`,plant_product WHERE plant_product.id=seller_demand.product_id GROUP BY plant_product.id "
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


def Fullfill_seller_demand(request, pk):
    if request.session.has_key('Distributoruid') & request.session.has_key('Distributoruname'):
        location = request.session.get('Distributorlocation')
    sql1 = "SELECT pp.id,SUM(sd.Quantity)as total_quantity From seller_demand AS sd INNER JOIN plant_product AS pp ON " \
           "sd.id=pp.id GROUP BY pp.id "
    posts1 = Seller_demand.objects.raw(sql1)[:50]
    product = Seller_fullfill_demand.objects.get(id=pk)
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


def view_invoice(request):
    return render(request, "bata/Dashboard/assets/seller/view_invoice.html")


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


def view_invoice(request):
    return render(request, "bata/Dashboard/assets/Distributor/view_invoice.html")


def Productlot_pickup(request):
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
        srh=0

    print(srh)
    track = Tracking_reports.objects.filter(tracking_id__icontains=srh)

    if track.count() == 0 and srh !=0:
        messages.warning(request, "No search results found. Please refine your query.")

    return render(request, 'bata/tracking.html', {'track': track})


