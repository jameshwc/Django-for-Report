from User.models import User
from django import forms
from django.shortcuts import render, render_to_response
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import ensure_csrf_cookie
from django.template import RequestContext
from System.models import ip_log

def IP_log(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    if 'uid' in request.session:
        user = User.objects.get(id=request.session['uid'])
    else:
        user = None
    current_url = request.get_full_path()
    data = ip_log(ip = ip, user = user,page=current_url)
    data.save()