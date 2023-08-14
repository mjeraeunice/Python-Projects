from django.shortcuts import render, get_object_or_404, redirect
from .models import Cart
from inventory.models import Product
from .forms import CartForm

def cart_list(request):
    cart_items = Cart.objects.filter(user=request.user)
    return render(request, 'cart/cart_list.html', {'cart_items': cart_items})

def cart_item_detail(request, item_id):
    cart_item = get_object_or_404(Cart, id=item_id, user=request.user)
    if request.method == 'POST':
        form = CartForm(request.POST, instance=cart_item)
        if form.is_valid():
            form.save()
            return redirect('cart:cart_list')
    else:
        form = CartForm(instance=cart_item)
    return render(request, 'cart/cart_detail.html', {'form': form, 'cart_item': cart_item})

def edit_cart_item(request, item_id):
    cart_item = get_object_or_404(Cart, id=item_id, user=request.user)
    if request.method == 'POST':
        form = CartForm(request.POST, instance=cart_item)
        if form.is_valid():
            form.save()
            return redirect('cart:cart_list')
    else:
        form = CartForm(instance=cart_item)
    return render(request, 'cart/edit_cart_item.html', {'form': form, 'cart_item': cart_item})

def remove_cart_item(request, item_id):
    cart_item = get_object_or_404(Cart, id=item_id, user=request.user)
    if request.method == 'POST':
        cart_item.delete()
        return redirect('cart:cart_list')
    return render(request, 'cart/remove_cart_item.html', {'cart_item': cart_item})
