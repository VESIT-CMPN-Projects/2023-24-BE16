from django.shortcuts import render

# Create your views here.
def womenWelfarePage(request):
    return render(request,'womenWelfareApp/womenWelfare.html')