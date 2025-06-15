from django.contrib import admin

from order.models import OrderModel, OrderItem

admin.site.register(OrderModel)
admin.site.register(OrderItem)
