from django import template

register = template.Library()

@register.filter
def capitalizee(value):
    return value.capitalize()
