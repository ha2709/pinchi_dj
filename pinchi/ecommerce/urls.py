# myapp/urls.py

from django.urls import path
from .views_folder.user import UserListView  # Import your view here
from .views_folder.registration import UserRegistrationView
from .views_folder.verification import VerifyEmail
from .views_folder.product import ProductListCreateAPIView, ProductDetailAPIView
from .views_folder.shopping_cart import view_cart, add_to_cart, remove_from_cart
from .views_folder.order import OrderCreateView, order_history

urlpatterns = [
    path('users/', UserListView.as_view(), name='user-list'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('email-verify/', VerifyEmail.as_view(), name='email-verify'),
    path('products/', ProductListCreateAPIView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailAPIView.as_view(), name='product-detail'),
    path('cart/', view_cart, name='view-cart'),
    path('cart/add/<int:product_id>/', add_to_cart, name='add-to-cart'),
    path('cart/remove/<int:product_id>/', remove_from_cart, name='remove-from-cart'),
    path('orders/create/', OrderCreateView.as_view(), name='create-order'),
    path('orders/history/', order_history, name='order-history'),


     

]
