from django.db import transaction
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.forms import ValidationError

from carts.models import CartModel
from order.forms import CreateOrderForm
from order.models import OrderModel, OrderItem




class OrderView(LoginRequiredMixin, FormView):
    template_name = 'order/orders.html'
    form_class = CreateOrderForm
    success_url = reverse_lazy('user:profile')

    def get_initial(self):
        obj = super().get_initial()
        obj['first_name'] = self.request.user.first_name
        obj['last_name'] = self.request.user.last_name
        obj['phone'] = self.request.user.phone
        return obj
    
    def form_valid(self, form):

        try:
            with transaction.atomic():
                user = self.request.user
                carts = CartModel.objects.filter(user=user)

                if not carts.exists():
                    messages.error(self.request, 'Ваша корзина пуста')
                    return redirect('order:order')
                
                if carts.exists():
                    order = OrderModel.objects.create(
                        user=user,
                        phone=form.cleaned_data['phone'],
                        address=form.cleaned_data.get('address', ''),
                        requires=form.cleaned_data['requires_delivery'],
                        pay=form.cleaned_data['payment_method'],
                        is_pay=False,
                    )
                for cart in carts:
                    product = cart.product
                    name = cart.product.name
                    price = cart.product.sell_price()
                    quantity = cart.quantity

                    if product.quantity < quantity:
                       raise ValidationError(f'Недостаточное количество товара {name} на складе.')
                    
                    OrderItem.objects.create(
                        order=order,
                        product=product,
                        name=name,
                        price=price,
                        quantity=quantity
                    )
                    product.quantity -= quantity
                    product.save()

                carts.delete()

                messages.success(self.request, 'Заказ оформлен')
                return redirect('user:profile')
            
        except ValidationError as err:
            messages.error(self.request, str(err))
            return redirect('order:order')

    def form_invalid(self, form):
        messages.error(self.request, 'Заполните все поля')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Order - page'
        return context
    