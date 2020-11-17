# Generated by Django 3.1.2 on 2020-11-17 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20201115_0155'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_donator',
            field=models.BooleanField(default=False, help_text='Designates whether this user should be treated as an Donator. ', verbose_name='Donator '),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'مدير المؤسسه'), (2, 'مشرف جمعيه رئيسيه'), (3, 'مشرف جمعيه تنمويه'), (4, 'مشرف متعاون'), (5, 'محتاج'), (6, 'متبرع')], help_text='User Role in A system ', null=True, verbose_name='User Type'),
        ),
    ]
