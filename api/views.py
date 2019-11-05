from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse
from System.models import no2name_querylog
from User.models import User
from No2Name.models import ntu_student
from Base.views import IP_log

def get_students(request):
    IP_log(request)
    query_types = ['cname', 'no', 'dpt', 'ename', 'gender']
    if request.method == 'GET' and 'username' in request.session \
        and 'query_type' in request.GET and 'query' in request.GET:
            error = []
            qtype = request.GET['query_type']
            if qtype not in query_types:
                error.append('query_type not in query_types')
            query = request.GET['query']
            if qtype == 'cname':
                student_list = ntu_student.objects.filter(chinese_name__icontains=query)
            elif qtype == 'no':
                student_list = ntu_student.objects.filter(student_no__icontains=query)
            elif qtype == 'dpt':
                student_list = ntu_student.objects.filter(department__icontains=query)
            elif qtype == 'ename':
                student_list = ntu_student.objects.filter(english_name__icontains=query)
            elif qtype == 'gender':
                student_list = ntu_student.objects.filter(gender__icontains=query)
            else:
                student_list = None
            if len(student_list) >= 1000:
                error.append('the length of data is over 1000')
                student_list = None
            user = User.objects.get(id=request.session['uid'])            
            log = no2name_querylog(query=query, user=user, query_type=qtype)
            students = serializers.serialize('json', student_list)
            return JsonResponse({'student': students, 'error': error})
    else:
        return JsonResponse({'error': 'User not logged in or parameters are not matched'})