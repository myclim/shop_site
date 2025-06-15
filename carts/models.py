from django.db import models
from user.models import UsersModel
from shop.models import ProductModel




class CartQueryset(models.QuerySet):

    def total_price(self):
        return sum(cart.product_price() for cart in self)
    
    def total_quantity(self):
        return sum(cart.quantity for cart in self) if self else 0
    
    
class CartModel(models.Model):
    user = models.ForeignKey(to=UsersModel, 
                            on_delete=models.CASCADE,
                            blank=True, null=True,
                            verbose_name='Пользователь')
    product = models.ForeignKey(to=ProductModel,
                            on_delete=models.CASCADE,
                            verbose_name='Продукт')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Время')

    objects = CartQueryset.as_manager()

    def product_price(self):
        return round(self.product.sell_price() * self.quantity, 2)
    
    def __str__(self):
        return f'{self.user.username} - {self.product.name}'

    class Meta:
        db_table = 'cart'
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'
