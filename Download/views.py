from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from Download.models import Download_file
from System.models import download_log
from User.models import User
from Report.views import IP_log

def download(request):
    IP_log(request)
    if 'username' in request.session:
        if request.method == 'GET' and 'filename' in request.GET:
            filename = request.GET['filename']
            f = Download_file.objects.get(filename=filename)
            response = HttpResponse(f.file, content_type='application/octet-stream')
            response['Content-Disposition'] = 'attachment; filename=%s' % f.file.name.split('/')[-1]
            f.download_counter += 1
            f.save()
            user = User.objects.get(id=request.session['uid'])
            log = download_log(filename=f, user=user)
            log.save()
            return response
        files = Download_file.objects.all()
        return render(request,"Download.html",locals())    
    not_login = True
    # name_list, file_list = zip(*((file.name, file.file) for file in Download_file.objects.all()))
    # return render_to_response("Download.html",locals(),RequestContext(request))
    return render(request,"Download.html",locals())    
