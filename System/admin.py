from django.contrib import admin
from System.models import update_log, download_log, ip_log, no2name_querylog

class Download_log_admin(admin.ModelAdmin):
    list_display = ('date','filename','user')
class IP_log_admin(admin.ModelAdmin):
    list_display = ('date','ip','user','page')
    search_fields = ['ip']

class no2name_querylog_admin(admin.ModelAdmin):
    list_display = ('date', 'query', 'user')


admin.site.register(update_log)
admin.site.register(download_log,Download_log_admin)
admin.site.register(ip_log,IP_log_admin)
admin.site.register(no2name_querylog, no2name_querylog_admin)
