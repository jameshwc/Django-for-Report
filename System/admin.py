from django.contrib import admin
from System.models import update_log, download_log

class Download_log_admin(admin.ModelAdmin):
    list_display = ('date','filename','user')

admin.site.register(update_log)
admin.site.register(download_log,Download_log_admin)
# Register your models here.
