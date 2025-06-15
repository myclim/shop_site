from django import template
from carts.models import CartModel




register = template.Library()


@register.simple_tag()
def user_cart(request):
    if not request.user.is_authenticated:
        return CartModel.objects.none()
    return CartModel.objects.filter(user=request.user).select_related('product')
