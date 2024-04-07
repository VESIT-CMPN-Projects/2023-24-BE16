# market/urls.py
from django.urls import path
from .views import buy_product, product_list, barter_request, create_product, make_barter_transaction, my_products,show_barter_requests

app_name = 'market'

urlpatterns = [
    path('product_list/', product_list, name='product_list'),
    path('barter_request/<int:product_id>/', barter_request, name='barter_request'),
    path('create_product/', create_product, name='create_product'),
    path('make_barter_transaction/<int:request_id>/', make_barter_transaction, name='make_barter_transaction'),
    path('my_products/', my_products, name='my_products'),
    path('buy_product/<int:product_id>/', buy_product, name='buy_product'),
    path('show_barter_requests/<int:product_id>/', show_barter_requests, name='show_barter_requests'),


]
