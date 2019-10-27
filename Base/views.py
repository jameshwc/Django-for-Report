from django.shortcuts import render, render_to_response
from django.http import HttpResponse, Http404, HttpResponsePermanentRedirect
from django.template import RequestContext
from Report.views import IP_log

def home(request):
    IP_log(request)
    return render(request,'Home.html',locals())
    #return render_to_response('Home.html',locals(),RequestContext(request))
    # return HttpResponse("Hello World!")

def blog(request):
    IP_log(request)
    return HttpResponsePermanentRedirect("https://blog.jameshsu.csie.org")

def cool(request):
    IP_log(request)
    return HttpResponsePermanentRedirect("https://cool.jameshsu.csie.org")