from django.urls import include, path
from . import views

urlpatterns = [
    path('get/students', views.get_students),
]