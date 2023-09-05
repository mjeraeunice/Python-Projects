from django.shortcuts import render , redirect
from .forms import ProductUploadForm
from .models import Product


# Create your views here.
def product_upload_view(request):
    if request.method =="POST" :
        form= ProductUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("products_list")
    else:
        form = ProductUploadForm()
        
    return render(request, 'inventory/product_upload.html', {'form': form})


def products_list(request):
    products = Product.objects.all()
    return render(request, 'inventory/products_list.html', {'products':products})


def product_detail(request, id):
    product = Product.objects.get(id=id)
    return render(request , 'inventory/product_detail.html',{'product':product})



def product_update_view(request, id):
    product = Product.objects.get(id=id)

    if request.method == 'POST':
        form = ProductUploadForm(request.POST, instance=product)

        if form.is_valid():
            form.save()
            return redirect("products_list")
    
    else:
        form = ProductUploadForm(instance=product)

    return render(request, "inventory/edit_product.html", {'form': form})

def delete_product(request, id):
    product= Product.objects.get(id=id)
    product.delete()
    return redirect("products_list")