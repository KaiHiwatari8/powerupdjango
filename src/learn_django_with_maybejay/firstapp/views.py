from django.shortcuts import render, get_object_or_404
from .models import Products
from .forms import ProductForm

# Create your views here.

def dynamic_lookup_view(request, product_id):
    obj = get_object_or_404(Products, id = product_id)
    context = {
        'my_objs':[obj],
    }
    return render(request, 'product/details.html', context)

def product_create_view(request):
    print(request.GET)
    print(request.POST)
    context = {}
    return render(request, 'product/newproduct.html', context)

# def product_create_view(request):
#     form = ProductForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = ProductForm()

#     context = {
#         'form':form
#     }
#     return render(request, 'product/newproduct.html', context)

def product_details_view(request):
    obj = Products.objects.all()

    objs = []
    for i in range(len(obj)):
        objs.append(obj[i])
    
    context = {
        'my_objs':objs
    }
    return render(request, 'product/details.html', context)