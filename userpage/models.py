from django.db import models
from product.models import Product
from django.contrib.auth.models import User
from django.urls import reverse

class Cart(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('order_now',args=[self.id,self.product.id])

class Order(models.Model):
   PAYMENT_CHOICES= (
      ('cash','Cash on Delivery'),
      ('esew','Esewa')
   )
   PAYMENT_STATUS=(
       ('pending','Pending'),
       ('completed','Completed')
   )
   ORDER_STATUS=(
       ('pending','Pending'),
       ('delevired','Delivered'),
       ('cancelled','Cancelled')
   )
   product = models.ForeignKey(Product,on_delete=models.CASCADE)
   user = models.ForeignKey(User,on_delete=models.CASCADE)
   quantity = models.IntegerField(default=1)
   address = models.CharField(max_length=200)
   phone = models.CharField(max_length=10)
   total_price=models.IntegerField()
   order_date =models.DateTimeField(auto_now_add=True)
   payment_method = models.CharField(max_length=10,choices=PAYMENT_CHOICES, default='cash')
   payment_status = models.CharField(max_length=10,choices=PAYMENT_STATUS, default='pending')
   order_status = models.CharField(max_length=10,choices=ORDER_STATUS, default='pending')
   

