from django.shortcuts import render
from .models import Product, Service, HardwareType

def home(request):
    products = Product.objects.all()
    recent_products = [product for product in products if product.recently_published()]
    services = Service.objects.all()
    hardware_types = HardwareType.objects.all()
    return render(request, 'main/home.html', {'hardware_types': hardware_types,
                                              'products': products,
                                              'services': services,
                                              'recent_products':recent_products})
def shop(request):
    products = Product.objects.all()
    """
        another possible way to get hardware types,filtered by products
        hardware_types = HardwareType.objects.filter(products__in=products).distinct()
    """
    hardware_types = HardwareType.objects.all()
    context = {'products': products, 'hardware_types': hardware_types,}
    return render(request, 'main/shop.html', context)
