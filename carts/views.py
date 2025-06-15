from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView
from carts.models import CartModel
from django.contrib.auth.mixins import LoginRequiredMixin

from shop.models import ProductModel





class CartView(LoginRequiredMixin, TemplateView):
    template_name = 'carts/carts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Cart - page'
        context['carts'] = CartModel.objects.filter(user=self.request.user).select_related('product')
        return context
    

class CartAdd(LoginRequiredMixin, CreateView):
    model = CartModel
    template_name = 'carts/carts.html'
    fields = []
    success_url = reverse_lazy('shop:catalog')

    def form_valid(self, form):
        product_id = ProductModel.objects.get(pk=self.kwargs['product_id'])
        user = self.request.user
        quantity = int(self.request.POST.get('quantity', 1))
        if product_id and user:
            cart_item, create = CartModel.objects.get_or_create(
                user=user,
                product=product_id,
                defaults={'quantity': quantity},
            )
        if not create:
            cart_item.quantity += quantity
            cart_item.save()
        return HttpResponseRedirect(self.request.META.get('HTTP_REFERER', '/'))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Cart - page'
        return context
    

def cart_remove(request, product_id):
    cart = CartModel.objects.get(id=product_id)
    cart.delete()
    return redirect(request.META.get('HTTP_REFERER', 'catalog'))
