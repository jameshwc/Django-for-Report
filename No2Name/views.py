from django.shortcuts import render
from Report.views import IP_log
from No2Name.models import ntu_student
from System.models import no2name_querylog
from User.models import User
from django.http import HttpResponseNotFound, Http404

def No2Name(request):
    IP_log(request)
    if 'username' in request.session:
        query_types = ['cname', 'no', 'dpt', 'ename', 'gender']
        if request.method == 'GET' and 'query_type' in request.GET and 'query' in request.GET:
            qtype = request.GET['query_type']
            if qtype not in query_types:
                raise Http404
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
            has = True if student_list else False
            rows = len(student_list)
            if rows > 1000:
                toomuch = True
            user = User.objects.get(id=request.session['uid'])
            log = no2name_querylog(query=query, user=user, query_type=qtype)
            log.save()
            return render(request,"No2Name.html",locals())
        elif request.method == 'GET':
            return render(request,"No2Name.html",locals())    
    not_login = True
    return render(request,"No2Name.html",locals())