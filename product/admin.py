from django.contrib import admin
from . models import Category
from .models import Product
# Register your models here.

# admin.site.register(category)
@admin.register(Category)

class CategoryAdmin(admin.ModelAdmin):
    list_display=('category_name','created_at','updated_at')
    list_filter=('created_at',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=('product_name','price','in_stock','description','category','created_at','updated_at')
    list_filter=('created_at',)
    list_editable=('in_stock','price')
