from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path('predict',views.predict_farming_income,name='predict_farming_income')
]
