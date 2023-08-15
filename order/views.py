# views.py
from django.shortcuts import render, get_object_or_404, redirect
from order.models import Order
from .forms import OrderForm

def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm()
    return render(request, 'order/create_order.html', {'form': form})

def edit_order(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)
    
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('order_detail', order_number=order_number)
    else:
        form = OrderForm(instance=order)

    return render(request, 'order/edit_order.html', {'form': form, 'order': order})

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'order/order_list.html', {'orders': orders})

def order_detail(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)
    return render(request, 'order/order_detail.html', {'order': order})

