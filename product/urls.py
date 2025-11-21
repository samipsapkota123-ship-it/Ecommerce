
from django.urls import path
from . import views

urlpatterns = [
    path('all-products/', views.product,name='product'),
    path('update-product/<int:product_id>/',views.update_product,name="update_product"),
    path('add-product/',views.add_product,name="add_product"),
    path('delete-product/<int:product_id>/',views.delete_product,name='delete-product'),

    path('all-categories/',views.categories,name='category'),
    path('update-category/<int:category_id>/',views.update_category,name="update_category"),
    path('add-category/',views.add_category,name="add_category"),
    path('delete-category/<int:category_id>/',views.delete_category,name='delete-category'),
    path('order_status/',views.order_status,name='order_status'),
    path('update_order_status/<int:order_id>/<str:action>/', views.update_order_status, name='update_order_status'),
    path('customers/',views.customer_list,name='customers')
    
    

]