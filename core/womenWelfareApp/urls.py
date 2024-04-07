from django.urls import path
from . import views

app_name = 'womenWelfareApp'

urlpatterns = [
    path('main/',views.womenWelfarePage,name='womenWelfarePage'),

]