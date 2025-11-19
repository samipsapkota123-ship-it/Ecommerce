from django.shortcuts import render,redirect
from product.models import Product
from django.contrib.auth.decorators import login_required
from userpage.models import Cart
from django.contrib import messages
from django.urls import reverse
def home_page(request):
    products= Product.objects.all().order_by("-created_at")[:8]
    return render(request,"userpage/homepage.html",{ 'products':products})

def all_products(request):
    Products=Product.objects.all()
    return render(request,"userpage/all-products.html",{
        "products":Products
    })

def product_detial(request,product_id):
    Products=Product.objects.get(id=product_id)
    return render(request,"userpage/product_detial.html",{
        "product":Products
    })


# add to cart
@login_required
def add_to_cart(request,product_id):
    user=request.user
    product= Product.objects.get(id=product_id)
    cart_item = Cart.objects.filter(user=user, product=product)

    if cart_item.exists():
        messages.add_message(request,messages.ERROR,'The product is already in a cart.')
        return redirect(reverse("product_detial",args=[product.id]))
    else:
        Cart.objects.create(
            product=product,
            user=user
        )
        messages.add_message(request,messages.SUCCESS,'The product is added in a cart.')
    return redirect("show_cart_items")

@login_required
def show_cart_items(request):
    user= request.user
    cart=Cart.objects.filter(user=user)
    return render(request,"userpage/cart_items.html",{"cart":cart})

def delete_cart_items(request,cart_id):
    cart_item = Cart.objects.get(id=cart_id, user=request.user)
    cart_item.delete()
    messages.add_message(request,messages.SUCCESS,'Product is deleted permanantly.')
    return redirect('show_cart_items')

def order_now(request):
    user = request.user
    cart_items = Cart.objects.filter(user=user)
    return render(request, "userpage/order_now.html", {"cart_items": cart_items})

