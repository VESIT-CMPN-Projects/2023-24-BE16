from django.urls import path
from . import views

app_name = 'homeApp'

urlpatterns = [
    path('main/',views.homePage,name='homePage'),
    
    

    
]