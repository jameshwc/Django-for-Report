from rest_framework import serializers

from Report.No2Name.models import ntu_student

class Ntu_Student_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ntu_student
        fields = ('chinese_name', 'department', 'student_no', 'gender')