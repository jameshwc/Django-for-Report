# Generated by Django 2.2 on 2019-05-30 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0005_auto_20190529_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='student_id',
            field=models.CharField(max_length=20),
        ),
    ]
