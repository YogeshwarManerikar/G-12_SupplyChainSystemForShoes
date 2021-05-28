from django.shortcuts import redirect, render
from .model.bata_plant import BATA_PLANT


def seller_dash(request):

    return render(request,"bata/Dashboard/assets/seller/seller_dash.html")

def bwdate_report_details(request):

    return render(request,"bata/Dashboard/assets/seller/bwdate_report_details.html")

def change_password(request):

    return render(request,"bata/Dashboard/assets/seller/change_password.html")

def profile(request):

    return render(request,"bata/Dashboard/assets/seller/profile.html")

def view_invoice(request):

    return render(request,"bata/Dashboard/assets/seller/view_invoice.html")
    
def Return_the_product(request):

    return render(request,"bata/Dashboard/assets/seller/Return_the_product.html")


def Demand_for_Product(request):

    return render(request,"bata/Dashboard/assets/seller/Demand_for_Product.html")


def Seller(request):
    if request.method == "POST":
        form = BATA_PLANT.objects.filter(email=request.POST["email"], password=request.POST["password"])
        user = BATA_PLANT.get_user_by_email(request.POST["email"])
        print(form)
        print(user)
        if form.count() > 0:
            request.session["uname"] =user.first_name
            request.session["uid"] = user.id
            print(request.session["uid"])
            return redirect('seller_dash')
        else:
            error_message = 'Email or Password invalid !!'
            return render(request, "bata/Login/Seller.html", {'error': error_message})

    else:
        return render(request, "bata/Login/Seller.html")