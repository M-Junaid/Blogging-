from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Product
from .forms import ProductForm

# Create your views here.

def product_list(request):

    products = Product.objects.all()
    return render(request, 'gallery/index.html', {'products': products})

def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'gallery/index2.html', {'product': product})

def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST,instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'gallery/edit_product.html', {'form': form})

def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'gallery/delete_product.html', {'product': product})

def home(request):
    return HttpResponse("Welcome to the Home Page of the Gallery App!")