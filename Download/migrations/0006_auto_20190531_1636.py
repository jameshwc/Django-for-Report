# Generated by Django 2.2 on 2019-05-31 08:36

import Download.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Download','0004_auto_20190531_0207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='download_file',
            name='file',
            field=models.FileField(storage=Download.models.OverwriteStorage(), upload_to='upload/Download Files'),
        ),
    ]
