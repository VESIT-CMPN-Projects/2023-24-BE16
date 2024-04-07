# market/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, BarterRequest, Transaction
from .forms import ProductForm, BarterRequestForm
from django.contrib.auth.decorators import login_required


def buy_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    # Assuming User model has email and phone_number fields
    seller = product.seller
    seller_info = {
        'username': seller.username,
        'email': seller.email,
        
    }

    context = {
        'product': product,
        'seller_info': seller_info,
    }

    return render(request, 'market/buy_product.html', context)


def product_list(request):
    other_users_products = Product.objects.exclude(seller=request.user)
    context = {'other_users_products': other_users_products}
    return render(request, 'market/product_list.html', context)

def barter_request(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        form = BarterRequestForm(request.POST)
        if form.is_valid():
            barter_request = form.save(commit=False)
            barter_request.requester = request.user
            barter_request.product = product
            barter_request.save()
            return redirect('market:product_list')
    else:
        form = BarterRequestForm()

    context = {'product': product, 'form': form}
    return render(request, 'market/barter_request.html', context)

@login_required
def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.seller = request.user  # Set the seller to the logged-in user
            product.save()
            return redirect('market:product_list')
    else:
        form = ProductForm()

    return render(request, 'market/create_product.html', {'form': form})

def make_barter_transaction(request, request_id):
    barter_request = get_object_or_404(BarterRequest, id=request_id)

    if request.method == 'POST':
        Transaction.objects.create(
            buyer=request.user,
            seller=barter_request.product.seller,
            product=barter_request.product,
            is_barter=True
        )
        barter_request.is_approved = True
        barter_request.save()
        return redirect('market:my_products')

    context = {'barter_request': barter_request}
    return render(request, 'market/make_barter_transaction.html', context)

def my_products(request):
    my_products = Product.objects.filter(seller=request.user)
    my_barter_requests = BarterRequest.objects.filter(product__seller=request.user, is_approved=False)

    context = {'my_products': my_products, 'my_barter_requests': my_barter_requests}
    return render(request, 'market/my_products.html', context)


def show_barter_requests(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    barter_requests = BarterRequest.objects.filter(product=product)

    context = {'product': product, 'barter_requests': barter_requests}
    return render(request, 'market/show_barter_requests.html', context)
