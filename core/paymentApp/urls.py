from django.urls import path
from . import views

urlpatterns = [
    path('utility/',views.utility,name='utility'),
    path('paymenthandler/', views.paymenthandler, name='paymenthandler'),

]