# Generated by Django 3.1.7 on 2021-04-08 10:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_model', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
    ]
