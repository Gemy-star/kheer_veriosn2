# Generated by Django 3.1.7 on 2021-03-09 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0023_paydonation'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursebag',
            name='logo',
            field=models.ImageField(null=True, upload_to='', verbose_name='لوجو الدوره'),
        ),
    ]