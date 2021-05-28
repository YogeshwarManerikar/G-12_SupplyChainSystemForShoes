from django.shortcuts import redirect, render
from .model.bata_plant import BATA_PLANT


def Distributor_dash(request):

    return render(request,"bata/Dashboard/assets/Distributor/Distributor_dash.html")

def bwdate_report_details(request):

    return render(request,"bata/Dashboard/assets/Distributor/bwdate_report_details.html")

def change_password(request):

    return render(request,"bata/Dashboard/assets/Distributor/change_password.html")

def profile(request):

    return render(request,"bata/Dashboard/assets/Distributor/profile.html")

def view_invoice(request):

    return render(request,"bata/Dashboard/assets/Distributor/view_invoice.html")
    
def Productlot_pickup(request):

    return render(request,"bata/Dashboard/assets/Distributor/Productlot_pickup.html")

def invoice_from_plant(request):

    return render(request,"bata/Dashboard/assets/Distributor/invoice_from_plant.html")





def Distributor(request):
    if request.method == "POST":
        form = BATA_PLANT.objects.filter(email=request.POST["email"], password=request.POST["password"])
        user = BATA_PLANT.get_user_by_email(request.POST["email"])
        print(form)
        print(user)
        if form.count() > 0:
            request.session["uname"] =user.first_name
            request.session["uid"] = user.id
            print(request.session["uid"])
            return redirect('Distributor_dash')
        else:
            error_message = 'Email or Password invalid !!'
            return render(request, "bata/Login/Distributor.html", {'error': error_message})

    else:
        return render(request, "bata/Login/Distributor.html")