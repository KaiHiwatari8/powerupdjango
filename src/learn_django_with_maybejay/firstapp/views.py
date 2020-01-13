from django.shortcuts import render, get_object_or_404, redirect
from .models import Products
from .forms import ProductForm

# Create your views here.

def dynamic_lookup_view(request, product_id):
    try:
        obj = get_object_or_404(Products, id = product_id)
    except Products.DoesNotExist:
        raise Http404
    context = {
        'my_objs':[obj],
    }
    return render(request, 'product/details.html', context)

# def product_create_view(request):
#     context = {}
#     return render(request, 'product/newproduct.html', context)

def product_delete_view(request, id):
    obj = get_object_or_404(Products, id=id)
    if request.method == 'POST':
        obj.delete()
        return redirect('/home/')
    context ={
        'object':obj,
    }
    return render(request, 'product/product_delete.html', context)

def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()

    context = {
        'form':form
    }
    return render(request, 'product/newproduct.html', context)

def product_details_view(request):
    obj = Products.objects.all()

    # objs = []
    # for i in range(len(obj)):
    #     objs.append(obj[i])
    
    context = {
        'my_objs':obj,
    }
    return render(request, 'product/details.html', context)

def product_list_view(request):
    obj = Products.objects.all()

    objs = []
    for i in range(len(obj)):
        objs.append(obj[i])
    
    context = {
        'my_objs':objs
    }
    return render(request, 'product/list.html', context)