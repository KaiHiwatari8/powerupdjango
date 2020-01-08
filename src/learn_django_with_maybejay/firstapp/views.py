from django.shortcuts import render
from .models import Products

# Create your views here.
def product_details_view(request):
    obj = Products.objects.get(id=1)
    # context={
    #     'title': obj.title,
    #     'description': obj.description,
    #     'price': obj.price,
    #     'active': obj.active,
    # }
    context = {
        'object':obj,
    }
    return render(request, 'product/details.html', context)