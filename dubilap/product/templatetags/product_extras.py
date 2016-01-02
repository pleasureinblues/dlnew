from django import template
from product.models import Brand, ProductProfile

register = template.Library()

@register.inclusion_tag('product/brand_list.html')
def get_brand_list(brand=None):
    return {'brand': Brand.objects.all(), 'act_brand': brand}
