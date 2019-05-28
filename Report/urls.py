"""Report URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from Base.views import home
from Download.views import download
from System.views import Update_log

urlpatterns = [
    url(r'home/',home),
    url(r'download/',download,None,'Download_url_name'),
    url(r'^admin/', admin.site.urls),
    url(r'^$',home,None,'Home_url_name'),
    url(r'^log/',Update_log),
]
