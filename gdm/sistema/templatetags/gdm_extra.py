from django.template import Library

register = Library()


@register.filter
def is_conected(arg):
    return arg is True


@register.filter
def not_conected(arg):
    return arg is (False or None)
