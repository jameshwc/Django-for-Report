from django.shortcuts import render, render_to_response
from System.models import update_log


def Update_log(request):
    log = update_log.objects.all()
    return render_to_response('Update_log.html',locals())