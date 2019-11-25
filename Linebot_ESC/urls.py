from django.urls import path
from . import views

urlpattens = [
    path('echo/', views.echo)
]