# Generated by Django 3.1.5 on 2021-01-19 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0017_auto_20210116_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='needycase',
            name='case_type',
            field=models.SmallIntegerField(blank=True, choices=[(1, 'دعم الكهرباء'), (2, 'دعم الغذاء'), (3, 'دعم التعليم'), (4, 'دعم الماء'), (5, 'دعم الصحة'), (6, 'دعم اﻷيجار')], null=True, verbose_name='نوع الحاله'),
        ),
    ]
