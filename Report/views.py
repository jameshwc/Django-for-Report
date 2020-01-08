from User.models import User
from django import forms
from django.shortcuts import render, render_to_response
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import ensure_csrf_cookie
from django.template import RequestContext
from django.http import Http404
from System.models import ip_log
from User.models import User
from django.contrib import admin


ALLOWED_IP_BLOCKS = ['127.0.0.1', '10.8.0.2', '52.229.61.229']

def login_by_ip(view_func):
    def authorize(request, *args, **kwargs):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        if ip in ALLOWED_IP_BLOCKS:
            return view_func(request, args, kwargs)
        raise Http404
    return authorize


def IP_log(request,url=None):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    if 'uid' in request.session:
        user = User.objects.get(id=request.session['uid'])
    else:
        user = None
    if url is None:
        url = request.get_full_path()
    data = ip_log(ip = ip, user = user,page=url)
    data.save()

def handler404(request, exception):
    IP_log(request)
    response = render(request, '404.html')
    response.status_code = 404
    return response

def handler500(request):
    IP_log(request)
    response = render(request, '404.html')
    response.status_code = 500
    return response