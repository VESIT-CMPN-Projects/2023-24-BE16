from . import views
from django.urls import path

app_name = 'govtServices'

urlpatterns = [
    path('servicePage/', views.servicePage, name= 'servicePage'),
    path('addService/',views.addService,name='addService')
   
]
