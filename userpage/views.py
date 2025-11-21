from django.shortcuts import render,redirect
from product.models import Product
from django.contrib.auth.decorators import login_required
from userpage.models import Cart,Order
from django.contrib import messages
from django.urls import reverse
from .forms import OrderForm
from django.views import View
import uuid
from .esewa_signature import genSha256


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

def order_now(request,cart_id,product_id):
    user=request.user
    product = Product.objects.get(id=product_id)
    cart=Cart.objects.get(id=cart_id)

    if request.method == "POST":
        form=OrderForm(request.POST)
        if form.is_valid():
         data = form.cleaned_data
         quantity = data['quantity']
         address = data['address']
         phone = data['phone']
         payment_method = data['payment_method']
         total_price = product.price * quantity

        order = Order.objects.create(
            product=product,
            user=user,
            quantity=quantity,
            address=address,
            phone=phone,
            payment_method=payment_method,
            total_price=total_price
        )

        if order.payment_method == "cash":
            cart.delete()
            return redirect('show_cart_items')
    
    
        elif order.payment_method == "esew":
            return redirect(reverse("esewa_form")+"?o_id="+str(order.id)+"&c_id="+str(cart.id))

    

    return render(request, "userpage/order_now.html", {
        'form':OrderForm,
        'product_name':product.product_name,
        'price':product.price,
        'product_image':product.image
        })

@login_required
def order_history(request):
   user=request.user
   orders =Order.objects.filter(user=user)
   return render(request,"userpage/order_history.html",{
      'orders':orders
   })
   

class EsewaView(View):
   
   def get(self,request,*args,**kwargs):
      o_id= request.GET.get('o_id')
      c_id= request.GET.get('c_id')
      cart= Cart.objects.get(id=c_id)
      order= Order.objects.get(id=o_id)

      uuid_val = uuid.uuid4()

      secret_key= '8gBm/:&EnhH.1/q'
      data_to_sign = f"total_amount={order.total_price},transaction_uuid={uuid_val},product_code=EPAYTEST"

      result = genSha256(secret_key,data_to_sign)

      data={
         'amount':order.product.price,
         'total_amount':order.total_price,
         'transaction_uuid':uuid_val,
         'product_code':'EPAYTEST',
         'signature':result
      }

      return render(request,"userpage/esewaform.html",{
         'order':order,
         'cart':cart,
         'data':data
      })

   