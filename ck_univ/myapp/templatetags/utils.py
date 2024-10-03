from django import template
from django.utils.http import urlsafe_base64_encode

register = template.Library()


@register.filter(is_safe=True)
def n_f(a):
    print(type(a))
    if a=="1":
        k=a+'st'
    elif a=="2":
        k=a+'nd'
    elif a=="3":
        k=a+'rd'
    elif a=="Full Payment":
        k=a
    else:
        k=a+'th'
    return k

@register.filter
def to_camel_case(value):
    words = value.split('_')
    return words[0] + ''.join(word.capitalize() for word in words[1:])