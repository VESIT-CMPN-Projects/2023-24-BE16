from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
   
    path('status/',views.home,name='home'),
    path('predict/', views.predict_poverty_status_view, name='predict_poverty_status_view'),
]