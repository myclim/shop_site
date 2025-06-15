from django.db import models

from shop.models import ProductModel
from user.models import UsersModel





class OrderQueryset(models.QuerySet):
    
    def total_price(self):
        return sum(cart.products_price() for cart in self)
    
    def total_quantity(self):
        return sum(cart.quantity for cart in self) if self else 0
    

class OrderModel(models.Model):

    user = models.ForeignKey(
        to=UsersModel, 
        on_delete=models.CASCADE,
        verbose_name="Пользователь"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    phone = models.CharField(max_length=10, verbose_name='Номер телефона')
    requires = models.BooleanField(default=False, verbose_name='Требуется доставка')
    address = models.CharField(max_length=150, verbose_name='Адресс доставки')
    pay = models.BooleanField(default=False, verbose_name='Оплата при получение')
    is_pay = models.BooleanField(default=False, verbose_name='Оплаченно')
    status = models.CharField(max_length=50, default='В обработке', verbose_name='Статус заказа')

    class Meta:
        db_table = 'order'
        verbose_name = 'Заказ'
        verbose_name_plural = 'Закаы'
    
    def __str__(self):
        return f'{self.pk} - {self.user.username}'
    

class OrderItem(models.Model):

    order = models.ForeignKey(to=OrderModel, on_delete=models.CASCADE, verbose_name='Заказ')
    product = models.ForeignKey(
        to=ProductModel,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='Продукт'
    )
    name = models.CharField(max_length=150, verbose_name='Название')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Цена')
    quantity = models.IntegerField(default=0, verbose_name='Количество')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        db_table = 'order_item'
        verbose_name = 'Проданный товар'
        verbose_name_plural = 'Проданные товары'
    
    bjects = OrderQueryset.as_manager()

    def product_price(self):
        return round(self.price * self.quantity, 2)
    
    def __str__(self):
        return f'{self.pk} - {self.product.name}'
    