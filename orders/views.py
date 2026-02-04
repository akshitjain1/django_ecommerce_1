from django.shortcuts import render, redirect, get_object_or_404
from main.models import Product
from django.contrib.auth.decorators import login_required
from .models import Order, OrderItem
from django.contrib import messages

# Create your views here.
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id = product_id)
    
    cart = request.session.get('cart',{})
    
    product_id = str(product.id)
    
    if product_id in cart:
        if cart[product_id]['quantity'] < product.quantity:
            cart[product_id]['quantity'] += 1
    else:
        cart[product_id] = {
            'name': product.name,
            'price': product.price,
            'quantity': 1,
            'image': product.image.url
        }
    if product.quantity <= 0:
        messages.error(request, "This product is out of stock.")
        return redirect('products')
    messages.success(request, "Item added to cart")

    request.session['cart'] = cart
    return redirect('cart')

def cart_view(request):
    cart = request.session.get('cart',{})
    
    total = 0
    for item in cart.values():
        total += item['price'] * item['quantity']
        
    return render(request, 'cart.html', {'cart': cart, 'total': total})


def remove_from_cart(request, product_id):
    cart = request.session.get('cart',{})
    product_id = str(product_id)
    
    if product_id in cart:
        del cart[product_id]
        messages.success(request, "Item removed from cart")
    request.session['cart'] = cart
    return redirect('cart')


@login_required
def place_order(request):
    cart = request.session.get('cart', {})

    if not cart:
        return redirect('products')

    # Create order
    order = Order.objects.create(user=request.user)

    for product_id, item in cart.items():
        product = Product.objects.get(id=product_id)

        # SAFETY CHECK
        if product.quantity < item['quantity']:
            return redirect('cart')

        # Create order item
        OrderItem.objects.create(
            order=order,
            product=product,
            quantity=item['quantity']
        )

        # UPDATE STOCK
        product.quantity -= item['quantity']
        product.save()

    order.is_completed = True
    order.save()
    messages.success(request, "Order placed successfully!")
    # CLEAR CART
    request.session['cart'] = {}

    return redirect('order_success')

@login_required
def order_success(request):
    return render(request, 'order_success.html')


def update_cart(request, product_id, action):
    cart = request.session.get('cart', {})
    product_id = str(product_id)

    if product_id in cart:
        if action == 'increase':
            cart[product_id]['quantity'] += 1

        elif action == 'decrease':
            cart[product_id]['quantity'] -= 1

            if cart[product_id]['quantity'] <= 0:
                del cart[product_id]

    request.session['cart'] = cart
    return redirect('cart')
