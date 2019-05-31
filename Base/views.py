from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext
# Create your views here.

def home(request):
    return render_to_response('Home.html',locals(),RequestContext(request))
    # return HttpResponse("Hello World!")