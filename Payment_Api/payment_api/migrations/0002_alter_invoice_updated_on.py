# Generated by Django 3.2 on 2021-04-19 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='updated_on',
            field=models.DateField(auto_now=True),
        ),
    ]