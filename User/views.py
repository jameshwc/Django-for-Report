from django.shortcuts import render, render_to_response
from User.models import User
from django import forms
from django.template import RequestContext
from django.template.loader import render_to_string
from django.core.mail import send_mail, EmailMultiAlternatives
from django.http import HttpRequest
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import ensure_csrf_cookie
import random
from datetime import datetime
from Report.views import IP_log
import requests

class User_register_form(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='密碼')
    class Meta:
        model = User
        fields = ['username', 'password','email',]
        labels = {
            'username' : '用戶名稱',
            'email' : 'E-mail (NTU only)'
        }
    def clean_email(self):
        content = self.cleaned_data['email']
        student_id = content.split('@',1)[0].upper() # 轉換b 為 B
        domain = content.split('@', 1)[1]
        if(domain not in ( "ntu.edu.tw", "csie.ntu.edu.tw") or student_id[0] != 'B' or student_id[1:].isdigit() == False):
            raise forms.ValidationError('非NTU信箱格式！')
        try:
            user = User.objects.get(student_id=student_id)
        except ObjectDoesNotExist:
            user = None
        if(user is not None):
            if(user.is_verified):
                raise forms.ValidationError('該學號已遭註冊！')
            if(not user.is_verified):
                user.delete()
        return student_id + '@' + domain
        # Didn't figure out why the following code doesn't work out.
    def clean_username(self):
        UserName = self.cleaned_data['username']
        special_char = "!@#$%^&*()><?/\\"
        for each in UserName:
            if each in special_char:
                raise forms.ValidationError('用戶名稱請勿包含特殊字元！')
        try:
            user = User.objects.get(username=UserName)
        except ObjectDoesNotExist:
            user = None
        if(user is not None):
            if(user.is_verified):
                raise forms.ValidationError('該用戶名已遭註冊！')
        return UserName



@ensure_csrf_cookie
def Register(request):
    IP_log(request)
    if request.method == 'POST' :
        form = User_register_form(request.POST)
        if form.is_valid():
            uname = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            student_id = email.split('@',1)[0].upper()
            code = ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789') for _ in range(15))
            u = User(username = uname, password = password, email = email, is_verified = False, student_id = student_id, code = code)
            u.save()
            #send email:
            vlink = request.get_host() + "/verify?email=" + email + "&code=" + code
            pass_code = "1559758205.6652055"
            data = {'random':pass_code, 'link':vlink, 'email':email, 'user':uname}
            is_sent = True
            r = requests.post('https://www.csie.ntu.edu.tw/~b07902001/mail.php', data=data)
            return render_to_response('Register.html',locals(), RequestContext(request))
        Error = True
        return render_to_response('Register.html',locals())
    else:
        form = User_register_form()
        return render_to_response('Register.html',locals(), RequestContext(request))


def Verify(request):
    IP_log(request)
    email = request.GET['email']
    code = request.GET['code']
    verify = User.objects.filter(email=email, code=code) or None
    if verify is None:
        fail = True
    else:
        fail = False
        verify.update(verified_time = datetime.now(), is_verified = True)
    return render_to_response('Verify.html',locals())

class Login_form(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='密碼')
    class Meta:
        model = User
        fields = ['username', 'password',]
        labels = {
            'username' : '用戶名稱 / E-mail',
        }

@ensure_csrf_cookie
def Login(request):
    IP_log(request)
    if request.method == 'POST':
        form = Login_form(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            if '@' in username:
                try:
                    username = username.capitalize()
                    query = User.objects.get(email=username, password=password)
                except ObjectDoesNotExist:
                    query = None
            else:
                try:
                    query = User.objects.get(username=username, password=password)
                except ObjectDoesNotExist:
                    query = None
            if query is None or query.is_verified == False:
                Fail = True
            else:
                request.session['username'] = query.username
                request.session['uid'] = query.id
                request.session.modified = True
                is_login = True
    else:
        form = Login_form()
    return render_to_response('Login.html',locals(),RequestContext(request))

def Logout(request):
    IP_log(request)
    if 'username' in request.session:
        logout = True
        del request.session['username']
        del request.session['uid']
        request.session.modified = True
        return render_to_response('Logout.html',locals(),RequestContext(request))
    logout = False
    return render_to_response('Logout.html',locals(),RequestContext(request))
