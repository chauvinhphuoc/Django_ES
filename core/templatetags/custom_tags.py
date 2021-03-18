from django import template
import json

register = template.Library()


@register.filter
def get_source(value):
    return value['_source']
