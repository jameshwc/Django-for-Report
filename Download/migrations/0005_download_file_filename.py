# Generated by Django 2.2 on 2019-05-31 07:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Download', '0004_auto_20190531_0207'),
    ]

    operations = [
        migrations.AddField(
            model_name='download_file',
            name='filename',
            field=models.CharField(default=django.utils.timezone.now, max_length=30),
            preserve_default=False,
        ),
    ]
