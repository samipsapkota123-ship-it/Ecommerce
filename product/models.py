from django.db import models

# Create your models here.
class Category(models.Model):
    category_name=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural="Categories"
        verbose_name="Category"

    def __str__(self):
        return self.category_name



class Product(models.Model):
    product_name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    description=models.TextField()
    in_stock=models.BooleanField(default=True)
    image=models.ImageField(upload_to='product_images',blank=True, null=True)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural="Products"
        verbose_name="Product"

    def __str__(self):
        return self.product_name