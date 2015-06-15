from django import template
from django.utils.safestring import mark_safe
import markdown2

register = template.Library()

@register.filter(name='markdown')
def markdown(value):
    return mark_safe(markdown2.markdown(value,extras=['fenced-code-blocks']))
