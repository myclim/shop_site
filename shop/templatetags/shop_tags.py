from django import template
from shop.models import CategoryModel, SubCategoryModel




register = template.Library()

@register.simple_tag()
def category_tags():
    return CategoryModel.objects.all()


@register.simple_tag()
def sub_category():
    return SubCategoryModel.objects.all()


@register.simple_tag
def url_replace(request, field, value):
    params = request.GET.copy()
    params[field] = value
    return params.urlencode()
