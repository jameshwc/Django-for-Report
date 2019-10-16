from django.db import models
from User.models import User

# Create your models here.
class Message(models.Model):
    author = models.ForeignKey(User,null=True,on_delete=models.SET_NULL)
    post_time = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=80)
    reply = models.ForeignKey('self',on_delete=models.SET_NULL,null=True)
    content = models.TextField()
    def __str__(self):
        return self.title