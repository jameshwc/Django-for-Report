from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage
class OverwriteStorage(FileSystemStorage):
    def get_available_name(self, name, max_length=None):
        if self.exists(name):
            os.remove(os.path.join(settings.MEDIA_ROOT, name))
        return name

class Download_file(models.Model):
    file = models.FileField(upload_to='upload/Download Files',storage=OverwriteStorage())
    init_upload_time = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    download_counter = models.IntegerField()
    name = models.CharField(max_length=30)
    filename = models.CharField(max_length=30, default='NaN')
    
    def __str__(self):
        return self.name

@receiver(post_delete, sender=Download_file)
def submission_delete(sender, instance, **kwargs):
    instance.file.delete(False) 
