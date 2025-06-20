from django import template
from django.core.cache import cache

from shop.models import CategoryModel, SubCategoryModel


register = template.Library()


@register.simple_tag()
def category_tags():
    cache_category = cache.get('category')
    if not cache_category:
        cache_category = CategoryModel.objects.all()
        cache.set('category', cache_category, 60)
    return cache_category


@register.simple_tag()
def sub_category():
    cache_sub_cateogry = cache.get('sub_category')
    if not cache_sub_cateogry:
        cache_sub_cateogry = SubCategoryModel.objects.all()
        cache.set('sub_category', cache_sub_cateogry, 60)
    return cache_sub_cateogry


@register.simple_tag
def url_replace(request, field, value):
    params = request.GET.copy()
    params[field] = value
    return params.urlencode()
