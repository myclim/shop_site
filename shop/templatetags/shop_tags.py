from django import template
from shop.models import CategoryModel




register = template.Library()

@register.simple_tag()
def category_tags():
    return CategoryModel.objects.all()

