from django.shortcuts import redirect, render
from .model.bata_plant import BATA_PLANT


def RM_dash(request):

    return render(request,"bata/Dashboard/assets/RM_provider/RM_dash.html")


def change_password(request):

    return render(request,"bata/Dashboard/assets/RM_provider/change_password.html")

def profile(request):

    return render(request,"bata/Dashboard/assets/RM_provider/profile.html")

def Consignments(request):

    return render(request,"bata/Dashboard/assets/RM_provider/Consignments.html")

    
def Requirment_for_RowMaterial(request):

    return render(request,"bata/Dashboard/assets/RM_provider/Requirment_for_RowMaterial.html")

def payment_history(request):

    return render(request,"bata/Dashboard/assets/RM_provider/payment_history.html")





def RM_provider(request):
    if request.method == "POST":
        form = BATA_PLANT.objects.filter(email=request.POST["email"], password=request.POST["password"])
        user = BATA_PLANT.get_user_by_email(request.POST["email"])
        print(form)
        print(user)
        if form.count() > 0:
            request.session["uname"] =user.first_name
            request.session["uid"] = user.id
            print(request.session["uid"])
            return redirect('RM_provider_dash')
        else:
            error_message = 'Email or Password invalid !!'
            return render(request, "bata/Login/RowMaterialProvider.html", {'error': error_message})

    else:
        return render(request, "bata/Login/RowMaterialProvider.html")