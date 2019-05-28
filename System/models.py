from django.db import models

# Create your models here.

class update_log(models.Model):
    date = models.DateField()
    is_content = models.BooleanField() # A log is either content update or system update.
    is_debug = models.BooleanField() # reserved for system log
    detail = models.CharField(max_length = 200)
