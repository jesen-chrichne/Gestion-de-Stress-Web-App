# Generated by Django 3.1.14 on 2022-04-09 13:30

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Webapp', '0005_auto_20220409_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news_post',
            name='Date_pub',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='news_post',
            name='Fichier',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(), upload_to=''),
        ),
    ]