from django.shortcuts import render, get_object_or_404, redirect
from .models import Delivery
from .forms import DeliveryForm

def create_delivery(request):
    if request.method == 'POST':
        form = DeliveryForm(request.POST)
        if form.is_valid():
            delivery = form.save()
            return redirect('delivery:delivery_detail', pk=delivery.pk)
    else:
        form = DeliveryForm()
    return render(request, 'delivery/create_delivery.html', {'form': form})

def edit_delivery(request, pk):
    delivery = get_object_or_404(Delivery, pk=pk)
    if request.method == 'POST':
        form = DeliveryForm(request.POST, instance=delivery)
        if form.is_valid():
            form.save()
            return redirect('delivery:delivery_detail', pk=pk)
    else:
        form = DeliveryForm(instance=delivery)
    
    context = {
        'form': form,
        'delivery': delivery,
    }
    return render(request, 'delivery/edit_delivery.html', context)

def delivery_list(request):
    deliveries = Delivery.objects.all()
    return render(request, 'delivery/delivery_list.html', {'deliveries': deliveries})

def delivery_detail(request, pk):
    delivery = get_object_or_404(Delivery, pk=pk)
    return render(request, 'delivery/delivery_detail.html', {'delivery': delivery})
