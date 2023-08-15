from django.shortcuts import render, redirect, get_object_or_404
from .models import Payment
from .forms import PaymentForm

def create_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save()
            return redirect('edit_payment', pk=payment.pk)
    else:
        form = PaymentForm()
    return render(request, 'payment/create_payment.html', {'form': form})


def edit_payment(request, pk):
    payment = get_object_or_404(Payment, pk=pk)
    if request.method == 'POST':
        form = PaymentForm(request.POST, instance=payment)
        if form.is_valid():
            form.save()
            return redirect('payment_detail', pk=pk)
    else:
        form = PaymentForm(instance=payment)
    return render(request, 'payment/edit_payment.html', {'form': form, 'payment': payment})

def payment_list(request):
    payments = Payment.objects.all()
    return render(request, 'payment/payment_list.html', {'payments': payments})

def payment_detail(request, pk):
    payment = get_object_or_404(Payment, pk=pk)
    return render(request, 'payment/payment_detail.html', {'payment': payment})