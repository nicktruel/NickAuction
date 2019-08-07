from django.shortcuts import render
from .models import Product

# Create your views here.
def all_products(request):
    """ Display the product page """
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})