from django.views.generic import DetailView, ListView
from django.core.cache import cache

from shop.models import ProductModel
from shop.utils import search_products




class ProductListView(ListView):
    model = ProductModel
    template_name = 'shop/shop_list.html'
    context_object_name = 'products'
    paginate_by = 9
    
    def get_queryset(self):
        queryset = super().get_queryset()
        search_text = self.request.GET.get('q', '')
        sub_list = self.request.GET.getlist('subcategories')

        if search_text:
            queryset = search_products(search_text)
            return queryset

        if sub_list:
            queryset = ProductModel.objects.filter(category__id__in=sub_list)
        return queryset
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        top_product = cache.get('top_product')
        if not top_product:
            top_product = ProductModel.objects.order_by('-discount').first()
            cache.set('top_product', top_product, 15 * 60)

        context["title"] = 'Blog - page'
        context['top_product'] = top_product
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
    