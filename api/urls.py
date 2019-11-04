from django.urls import include, path
from . import views

urlpatterns = [
    path('get/student', views.get_students),
]