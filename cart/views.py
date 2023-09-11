from django.shortcuts import render, redirect
from .models import Product_Cart
from datetime import datetime
from .models import Product
from django.contrib import messages
from django.urls import reverse
from order.models import Order  
from .forms import CartUploadForm  

def view_cart(request):
    product_cart = Product_Cart.objects.all()
    
    total_cart_price = 0

    for item in product_cart:
        item.total_price = item.product_price * item.product_quantity
        total_cart_price += item.total_price

    return render(request, "cart/view_cart.html", {"product_cart": product_cart, "total_cart_price": total_cart_price})

def update_cart(request, id):
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        cart_item = Product_Cart.objects.get(id=id)
        if quantity > 0:
            cart_item.product_quantity = quantity
            cart_item.save()
        else:
            cart_item.delete()
    return redirect('view_cart')

def remove_item(request, id):
    cart_item = Product_Cart.objects.get(id=id)
    cart_item.delete()
    return redirect('view_cart')

def empty_cart(request):
    Product_Cart.objects.all().delete()
    return redirect("view_cart")

def add_to_cart(request, id):
    product = Product.objects.get(id=id)

    cart_item_exists = Product_Cart.objects.filter(product_name=product.name).exists()

    if not cart_item_exists:
        cart_item = Product_Cart (
            product_name = product.name,
            product_price = product.price,
            product_image = product.image,
            product_quantity = 1,
            date_added=datetime.now(),
        )
        cart_item.save()
        
        messages.success(request, f"{product.name} added to cart successfully.")
    else:
        messages.warning(request, f"{product.name} is already in your cart.")

    return redirect(reverse("products_list"))

def checkout_view(request):
    if request.method == 'POST':
        form = CartUploadForm(request.POST)
        if form.is_valid():
            order = Order.objects.create(
                user=request.user,  
                order_date=datetime.now(),
            )

            product_cart = Product_Cart.objects.all()

            for item in product_cart:
                order.order_items.create(
                    product_name=item.product_name,
                    product_price=item.product_price,
                    product_quantity=item.product_quantity,
                )

            Product_Cart.objects.all().delete()

            return render(request, "cart/checkout_success.html", {"order": order})

    else:
        form = CartUploadForm()

    return render(request, "cart/checkout.html", {"form": form})
