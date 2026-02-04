from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import user_passes_test
from main.models import Product
from orders.models import Order
from django.core.paginator import Paginator


def admin_login(request):
    if request.method == "POST":
        user = authenticate(
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user and user.is_staff:
            login(request, user)
            return redirect('admin_dashboard')
    return render(request, 'admin/login.html')


@user_passes_test(lambda u: u.is_staff)
def admin_dashboard(request):
    products = Product.objects.count()
    orders = Order.objects.count()
    low_stock = Product.objects.filter(quantity__lt=5).count()

    return render(request, 'admin/dashboard.html', {
        'products': products,
        'orders': orders,
        'low_stock': low_stock
    })

@user_passes_test(lambda u: u.is_staff)
def admin_products(request):
    product_list = Product.objects.all().order_by('-id')

    paginator = Paginator(product_list, 10)  # 10 per page
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)

    return render(request, 'admin/products.html', {'products': products})


@user_passes_test(lambda u: u.is_staff)
def admin_add_product(request):
    if request.method == "POST":
        Product.objects.create(
            name=request.POST['name'],
            price=request.POST['price'],
            quantity=request.POST['quantity'],
            description=request.POST['description'],
            image=request.FILES['image']
        )
        return redirect('admin_products')

    return render(request, 'admin/add_product.html')

@user_passes_test(lambda u: u.is_staff)
def admin_edit_product(request, id):
    product = Product.objects.get(id=id)

    if request.method == "POST":
        product.name = request.POST['name']
        product.price = request.POST['price']
        product.quantity = request.POST['quantity']
        product.description = request.POST['description']

        if 'image' in request.FILES:
            product.image = request.FILES['image']

        product.save()
        return redirect('admin_products')

    return render(request, 'admin/edit_product.html', {'product': product})

@user_passes_test(lambda u: u.is_staff)
def admin_delete_product(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('admin_products')


@user_passes_test(lambda u: u.is_staff)
def admin_orders(request):
    orders = Order.objects.all().order_by('-created_at')
    return render(request, 'admin/orders.html', {'orders': orders})

@user_passes_test(lambda u: u.is_staff)
def admin_order_detail(request, id):
    order = Order.objects.get(id=id)
    return render(request, 'admin/order_detail.html', {'order': order})
