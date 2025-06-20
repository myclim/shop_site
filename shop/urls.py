from django.urls import path
from shop.views import ProductListView, ProductSingleView




app_name = 'shop'

urlpatterns = [
    path('search/', ProductListView.as_view(), name='search'),
    path('', ProductListView.as_view(), name='catalog'),
    path('prudct/<slug:product_slug>/', ProductSingleView.as_view(), name='product'),
]
