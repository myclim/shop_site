from carts.models import CartModel



def get_user_cart(request):
    if request.user.is_authenticated:
        return CartModel.objects.filter(user=request.user).select_related('product')