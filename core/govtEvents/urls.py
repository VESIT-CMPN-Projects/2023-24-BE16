from . import views
from django.urls import path

app_name = 'govtEvents'

urlpatterns = [
    path('eventPage/',views.eventPage, name='eventPage'),
    path('addEvent/',views.addEvent,name='addEvent')
   
]
