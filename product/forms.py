from django import forms
from .models import Category,Product


class CategoryForm(forms.ModelForm):
    
    class Meta:
        model = Category
        fields = ['category_name']


    def clean_categroy_name(self):
        category_name = self.cleaned_data['category_name']
        if Category.objects.filter(category_name = category_name).exists():
            raise forms.ValidationError("Category name already exists")
        return category_name

class ProductForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = ['product_name','price','description','in_stock','image','category']


    def clean_product_name(self):
        product_name = self.cleaned_data['product_name']
        if Product.objects.filter(product_name = product_name).exists():
            raise forms.ValidationError("Product name already exists")
        return product_name
    
    