from django.db import models

class ntu_student(models.Model):
    department = models.CharField(max_length=30)
    student_no = models.CharField(max_length=30, primary_key=True)
    gender = models.CharField(max_length=10)
    chinese_name = models.CharField(max_length=50)
    english_name = models.CharField(max_length=50)

    def __str__(self):
        return self.chinese_name