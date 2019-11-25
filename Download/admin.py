from django.contrib import admin
from Download.models import Download_file

class Download_file_admin(admin.ModelAdmin):
    list_display=('name','init_upload_time', 'last_modified', 'download_counter')

# Register your models here.
admin.site.register(Download_file,Download_file_admin)