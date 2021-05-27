from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404

from .forms import Add_product, RawDemand, Add_rawmaterial, editproduct, editrawproduct
from .model import Raw_Demand, Product, Raw_Product
from .model.bata_plant import BATA_PLANT
from .model.seller import Seller


def plant_dash(request):
    if request.session.has_key('uid') & request.session.has_key('uname'):
        user = request.session.get('uid')
        print("location haii..................")
        return render(request, 'bata/Dashboard/assets/plantadmin/dashboard.html',
                      {'user': request.session["uname"], 'id': user})
    else:
        return redirect('plant_login')

def seller_dash(request):
    if request.session.has_key('uid') & request.session.has_key('uname'):
        user = request.session.get('uid')
        print("location haii..................")
        return render(request, 'bata/Dashboard/assets/seller/dashboard.html',
                      {'user': request.session["uname"], 'id': user})
    else:
        return redirect('seller_login')


def addcategory(request):

    return render(request,"bata/Dashboard/assets/plantadmin/add-category.html")


def stage_one_product_lot(request):
    return render(request, "bata/Dashboard/assets/plantadmin/1st-stage-productlot.html")


def stage_one_RowMaterial_lot(request):
    sql = "SELECT * FROM rawmaterial_demand where rawmaterial_demand.status = 'RECEIVED'"
    posts = Raw_Demand.objects.raw(sql)[:10]

    return render(request, "bata/Dashboard/assets/plantadmin/1st-stage-RowMaterial-lot.html",{'detail':posts})


def addp_roduct(request):
    context = {}
    if request.session.has_key('uid') & request.session.has_key('uname'):
        user = request.session.get('uid')
        uname = request.session.get('uname')
        print(user,uname)
    # create object of form
    form = Add_product(request.POST)



    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()
        messages.success(request, 'Product Succesfully added')

        return redirect('addp_roduct')

    return render(request, "bata/Dashboard/assets/plantadmin/add-product.html",{'id': request.session.get('uid'),'form':form})


def add_rawmaterial_category(request):


    if request.session.has_key('uid') & request.session.has_key('uname'):
        user = request.session.get('uid')
        uname = request.session.get('uname')
        print(user,uname)
    # create object of form
    form = Add_rawmaterial(request.POST)



    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()
        messages.success(request, 'Raw Material Succesfully added')

        return redirect('add_rawmaterial_category')
    return render(request, "bata/Dashboard/assets/plantadmin/add-rawmaterial-category.html",{'id': request.session.get('uid'),'form':form})


def bwdate_report_details(request):
    return render(request, "bata/Dashboard/assets/plantadmin/bwdate-report-details.html")


def bwdate_report_ds(request):
    return render(request, "bata/Dashboard/assets/plantadmin/bwdate-report-ds.html")


def change_password(request):
    return render(request, "bata/Dashboard/assets/plantadmin/change-password.html")


def Demand_for_Rowmaterial(request):

    if request.session.has_key('uid') & request.session.has_key('uname'):
        user = request.session.get('uid')
        uname = request.session.get('uname')
        print(user,uname)
    # create object of form
    form = RawDemand(request.POST)

    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()
        messages.success(request, 'Product Succesfully added')

        return redirect('Demand_for_Rowmaterial')
    print(form)
    return render(request, "bata/Dashboard/assets/plantadmin/Demand-for-Rowmaterial.html",{'id': request.session.get('uid'),'location':request.session.get('location'),'form':form})


def edit_category(request):
    return render(request, "bata/Dashboard/assets/plantadmin/edit-category.html")

def edit_product(request, pk):

    if request.session.has_key('uid') & request.session.has_key('uname'):
        user = request.session.get('uid')
        uname = request.session.get('uname')
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
    if request.session.has_key('uid') & request.session.has_key('uname'):
        user = request.session.get('uid')
        uname = request.session.get('uname')
        print(user, uname)
    sql = "SELECT * FROM plant_product where plant_product.user_id_id ='%s' "% user
    posts = Product.objects.raw(sql)[:50]


    return render(request, "bata/Dashboard/assets/plantadmin/Manage_product.html",{'detail':posts})


def edit_Rowmaterial_categories(request, pk):
    if request.session.has_key('uid') & request.session.has_key('uname'):
        user = request.session.get('uid')
        uname = request.session.get('uname')
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
    if request.session.has_key('uid') & request.session.has_key('uname'):
        user = request.session.get('uid')
        uname = request.session.get('uname')
        print(user, uname)
    sql = "SELECT * FROM rawmaterial_product where rawmaterial_product.user_id_id ='%s' " % user
    posts = Raw_Product.objects.raw(sql)[:50]

    return render(request, "bata/Dashboard/assets/plantadmin/manage-Rowmaterial-categories .html", {'detail': posts})



def Manage_invoice(request):
    if request.session.has_key('uid') & request.session.has_key('uname'):
        user = request.session.get('uid')
        uname = request.session.get('uname')
        print(user, uname)
    sql = "SELECT * FROM rawmaterial_demand where rawmaterial_demand.status ='RECEIVED' and " \
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
    return render(request, "bata/Dashboard/assets/plantadmin/returnproduct.html")


def Rowmaterial_Payment(request):
    sql = "SELECT * FROM rawmaterial_demand where rawmaterial_demand.status ='DISPATCHED'"
    sql1 = "SELECT * FROM rawmaterial_demand where rawmaterial_demand.status ='PENDING'"
    posts = Raw_Demand.objects.raw(sql)[:50]
    posts1 = Raw_Demand.objects.raw(sql1)[:50]

    return render(request, "bata/Dashboard/assets/plantadmin/Rowmaterial-Payment.html",{'detail':posts,'details':posts1})


def RowMaterial_payment_status_update(request):
    return render(request, "bata/Dashboard/assets/plantadmin/RowMaterial-payment-status-update.html")


def sales_report_details(request):
    return render(request, "bata/Dashboard/assets/plantadmin/sales-report-details.html")


def sales_report_ds(request):
    return render(request, "bata/Dashboard/assets/plantadmin/sales-report-ds.html")





def Plant_login(request):
    if request.method == "POST":
        form = BATA_PLANT.objects.filter(email=request.POST.get("email"), password=request.POST.get("password"))
        user = BATA_PLANT.get_user_by_email(request.POST.get("email"))

        print(form)
        if form.count() > 0:
            request.session["uname"] =user.first_name
            request.session["uid"] = user.id
            request.session["location"] = user.location
            print(request.session["uid"])
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
            request.session["uname"] =user.first_name
            request.session["uid"] = user.id
            print(request.session["uid"])
            return redirect('seller_dash')
        else:
            error_message = 'Email or Password invalid !!'
            return render(request, "bata/Login/Plant_admin.html", {'error': error_message})

    else:
        return render(request, "bata/Login/Seller.html")


def Seller_logout(request):
    request.session.clear()
    return redirect('Seller_login')