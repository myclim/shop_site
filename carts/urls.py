from django.urls import path
from carts.views import CartView, CartAdd, cart_remove



app_name = 'cart'

urlpatterns = [
    path('', CartView.as_view(), name='user_cart'),
    path('cart_add/<int:product_id>/', CartAdd.as_view(), name='cart_add'),
    path('cart_remove/<int:product_id>/', cart_remove, name='cart_remove')
]
