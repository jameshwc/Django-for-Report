from django import template
from django.urls import reverse

register = template.Library()

@register.simple_tag
def is_active(request,urls):
    if request in (reverse(url) for url in urls.split()):
        return "active"
    
    return ""
