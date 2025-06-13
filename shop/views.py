from django.shortcuts import render
from django.views.generic import DetailView, ListView
from shop.models import ProductModel




class ProductListView(ListView):
    model = ProductModel
    template_name = 'shop/shop_list.html'
    context_object_name = 'products'
    paginate_by = 9

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Blog - page'
        context['top_product'] = ProductModel.objects.order_by('-discount').first()
        return context


class ProductSingleView(DetailView):
    model = ProductModel
    template_name = 'shop/product_page.html'
    context_object_name = 'product'
    slug_url_kwarg = 'product_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Product - page'
        return context
    