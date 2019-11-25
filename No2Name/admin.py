from django.contrib import admin
from No2Name.models import ntu_student


class ntu_student_admin(admin.ModelAdmin):
    list_display = ('chinese_name','department','student_no','gender')
    search_fields = ['chinese_name', 'student_no']

admin.site.register(ntu_student, ntu_student_admin)