from django.urls import path
from . import views

urlpatterns = [
    path('', views.getProducts, name='get_products'),
    path('create', views.createProduct, name='create_product'),
    path('update/<str:pk>', views.updateProduct, name='update_product'),
    path('delete/<str:pk>', views.deleteProduct, name='delete_product'),
    path('<str:pk>', views.getProduct, name='get_product'),
]