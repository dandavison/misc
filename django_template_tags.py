#WIP
from django import template

register = template.Library()
template.libraries['django.templatetags.mytest'] = register


def custom_tag():
    return 'content from custom_tag'



register.tag(name='custom_tag', compile_function=custom_tag)
