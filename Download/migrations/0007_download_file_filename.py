# Generated by Django 2.2.2 on 2019-08-06 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Download', '0006_auto_20190531_1636'),
    ]

    operations = [
        migrations.AddField(
            model_name='download_file',
            name='filename',
            field=models.CharField(default='NaN', max_length=30),
        ),
    ]
