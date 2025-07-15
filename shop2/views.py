from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Cart, CartItem

def product_list(request):
    products = Product.objects.all()
    return render(request, 'shop/product_list.html', {'products': products})

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(id=1)  # For now, single cart
    item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    item.quantity += 1
    item.save()
    return redirect('view_cart')

def view_cart(request):
    cart = Cart.objects.get(id=1)
    items = CartItem.objects.filter(cart=cart)
    return render(request, 'shop/cart.html', {'items': items})
