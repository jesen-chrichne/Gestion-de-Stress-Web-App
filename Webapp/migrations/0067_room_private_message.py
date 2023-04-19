# Generated by Django 4.0.4 on 2022-07-10 18:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Webapp', '0066_remove_message_received_msg'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Theme', models.CharField(blank=True, max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Private_Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Message', models.CharField(max_length=1000)),
                ('Date', models.DateTimeField(auto_now=True)),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Webapp.utilisateur')),
            ],
        ),
    ]
