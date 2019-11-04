from django.shortcuts import render

from rest_framework import viewsets
from .serializers import Ntu_Student_serializer
from No2Name.models import ntu_student

class StudentViewSet(viewsets.ModelViewSet):
    queryset = ntu_student.objects.all().order_by('student_no')
    serializer_class = Ntu_Student_serializer