from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from Report.views import IP_log

def home(request):
    IP_log(request)
    return render_to_response('Home.html',locals(),RequestContext(request))
    # return HttpResponse("Hello World!")