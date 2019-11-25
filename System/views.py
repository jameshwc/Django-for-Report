from django.shortcuts import render, render_to_response
from System.models import update_log
from Report.views import IP_log
from django.template import RequestContext

def Update_log(request):
    IP_log(request)
    log = update_log.objects.all()
    return render(request,'Update_log.html',locals())

def External_link(request):
    try:
        url = request.POST['url']
    except:
        url = "Error"
    IP_log(request,url)