from django.db import models

class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=64)
    student_id = models.CharField(max_length=20)
    email = models.EmailField()
    is_verified = models.BooleanField()
    code = models.CharField(max_length=15)
    register_time = models.DateTimeField(auto_now_add=True)
    verified_time = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return self.student_id