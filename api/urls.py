from django.urls import path
from rest_framework.routers import DefaultRouter

from api.views import *




router = DefaultRouter()
app_name = 'api'

urlpatterns = [
    path('products/', AllProductApi.as_view(), name='product-list'),
    path('products/<int:pk>/', DetailProductApi.as_view(), name='product-detail'),
    path('categories/', AllCategoryApi.as_view(), name='category-list'),
    path('categories/<int:pk>/', DetailCategoryApi.as_view(), name='category-detail'),
    path('sub-categories/', AllSubCategoryApi.as_view(), name='subcategory-list'),
    path('sub-categories/<int:pk>/', DetailSubCategoryApi.as_view(), name='subcategory-detail'),
] + router.urls