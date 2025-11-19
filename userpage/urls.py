from django.urls import path
from . import views

urlpatterns=[
    path('',views.home_page,name="homepage"),
    path('all-products/',views.all_products,name="all-products"),
    path('product_detial/<int:product_id>',views.product_detial,name="product_detial"),
    path('add_to_cart/<int:product_id>',views.add_to_cart,name="add_to_cart"),
    path('show_cart_items/',views.show_cart_items,name="show_cart_items"),
    path('delete_cart_items/<int:cart_id>',views.delete_cart_items,name='delete_cart_items'),
    path('order_now/',views.order_now,name="order_now")
]