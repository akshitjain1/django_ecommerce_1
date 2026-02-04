from django.shortcuts import render
from .models import Product
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    return render(request, 'index.html')

def products(request):
    product_list = Product.objects.filter(is_active=True).order_by('-id')

    paginator = Paginator(product_list, 6)  # 6 products per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'products.html', {'items': page_obj})



def product_detail(request, id):
    product = get_object_or_404(Product, id=id, is_active=True)
    return render(request, 'product_detail.html', {'product': product})