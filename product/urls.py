
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
    
    

]