from django.db import models
from Download.models import Download_file
from User.models import User
# Create your models here.

class update_log(models.Model):
    date = models.DateField()
    is_content = models.BooleanField() # A log is either content update or system update.
    is_debug = models.BooleanField() # reserved for system log
    detail = models.CharField(max_length = 200)
    def __str__(self):
        return self.detail

class download_log(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    filename = models.ForeignKey(Download_file, null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

class ip_log(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    ip = models.GenericIPAddressField()
    user = models.ForeignKey(User,null=True, on_delete=models.SET_NULL)
    page = models.URLField()

class no2name_querylog(models.Model):
    student_info = (
        ('cname', 'chinese_name'),
        ('ename', 'english_name'),
        ('dpt', 'department'),
        ('gender', 'gender'),
        ('no', 'student_no')
    )
    date = models.DateTimeField(auto_now_add=True)
    query = models.CharField(max_length=50)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    query_type = models.CharField(max_length=30, choices=student_info)