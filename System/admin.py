from django.contrib import admin
from System.models import update_log, download_log, ip_log

class Download_log_admin(admin.ModelAdmin):
    list_display = ('date','filename','user')
class IP_log_admin(admin.ModelAdmin):
    list_display = ('date','ip','user','page')
    search_fields = ['ip']

admin.site.register(update_log)
admin.site.register(download_log,Download_log_admin)
admin.site.register(ip_log,IP_log_admin)
