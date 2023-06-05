from django import template
from main.models import *

register = template.Library()

@register.simple_tag()
def get_categories():
    return PropertyType.objects.all()

@register.inclusion_tag('main/list_categories.html')
def show_categories(sort=None, cat_selected=0):
    if not sort:
        cats = PropertyType.objects.all()
    else:
        cats = PropertyType.objects.order_by(sort)

    return {"cats": cats, "cat_selected": cat_selected}