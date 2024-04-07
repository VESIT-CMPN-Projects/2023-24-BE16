from django.shortcuts import render,redirect
from .models import saveService

# Create your views here.
def servicePage(request):
    servicesData = saveService.objects.all()
    print(servicesData)
    return render(request,'govtServices/services.html',context={'governmentServices':servicesData})


def addService(request):
    if request.method == "POST":
        service_name = request.POST['serviceName']
        service_description = request.POST['serviceDescription']
        service_contact = request.POST['serviceContact']
        en = saveService(service_name=service_name,service_description=service_description,service_contact=service_contact)
        en.save()
    return redirect("http://localhost:8000/govtServices/servicePage/")

