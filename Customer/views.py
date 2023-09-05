from django.shortcuts import render, get_object_or_404, redirect
from Customer.models import Customer
from .forms import CustomerForm

def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES)
        if form.is_valid():
            customer = form.save(commit=False)
            user = request.user
            customer.user = user
            customer.save()
            return redirect('customer_list')
    else:
        form = CustomerForm()
    return render(request, 'customer/create_customer.html', {'form': form})

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customer/customer_list.html', {'customers': customers})

def customer_detail(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    return render(request, 'customer/customer_details.html', {'customer': customer})

def edit_customer(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_list')  # Redirect to customer list view
    else:
        form = CustomerForm(instance=customer)
    
    return render(request, 'customer/edit_customer_details.html', {'form': form, 'customer': customer})
