import os
import csv
from models import ntu_Student

with open('No2Name/students.csv', 'r') as csvfile:
    rows = csv.reader(csvfile)
    for row in rows:
        student = ntu_student(department=row[1], student_no=row[3],\
                            gender=row[5], chinese_name=row[4], english_name=row[7])
        try:
            student.save()
        except:
            print('ERROR!')
