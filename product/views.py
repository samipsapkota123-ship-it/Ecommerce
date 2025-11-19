from django.shortcuts import render,redirect
from .models import Product,Category
from .forms import CategoryForm,ProductForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from Accounts.auth import admin_only

@login_required
@admin_only
def dashboard(request):
    return render(request,"dashboard/dashboard.html")

@login_required
@admin_only
def product(request):
    Products=Product.objects.all()
    return render(request,"product/product.html",{
        "products":Products
    })

@login_required
@admin_only
def update_product(request,product_id):
    product=Product.objects.get(id=product_id)
    
        # to send a data from form 
    if request.method == 'POST':
        form = ProductForm(request.POST,request.FILES, instance=product)
        
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'Product is updated')
            return redirect('product')
        else:
            return render(request,"product/update.product.html",{
        'form': form
    })
    return render(request,"product/update.product.html",{
        'form': ProductForm(instance=product)
    })

@login_required
@admin_only
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST,request.FILES)
        
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'New product is added.')
            return redirect('product')
        else:
            return render(request,"product/add_product.html",{
        'form': form
    })
    return render(request,"product/add_product.html",{
        'form': ProductForm()
    })

  
@login_required
@admin_only
def delete_product(request,product_id):
    product = Product.objects.get(id=product_id)
    product.delete()
    messages.add_message(request,messages.SUCCESS,'Product is deleted permanantly.')
    return redirect('product')

@login_required
@admin_only
def categories(request):
    category=Category.objects.all()
    return render(request,"product/category.html",{
        "category":category

    })

@login_required
@admin_only
def update_category(request,category_id):
    category = Category.objects.get(id=category_id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)

        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'Category is updated')
            return redirect('category')
        else:
        
            return render(request,"product/update-category.html",{
        'form': form
    })
    return render(request,"product/update-category.html",{
        'form': CategoryForm(instance=category)
    })

@login_required
@admin_only
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST,request.FILES)
        
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'New Category is added.')
            return redirect('category')
        else:
        
            return render(request,"product/add_category.html",{
        'form': form
    })
    return render(request,"product/add_category.html",{
        'form': CategoryForm()
    })

@login_required
@admin_only
def delete_category(request,category_id):
    category = Category.objects.get(id=category_id)
    category.delete()
    messages.add_message(request,messages.SUCCESS,'Category is deleted permanantly.')
    return redirect('category')




# form
# get => show date to client => form
# post => send data to server