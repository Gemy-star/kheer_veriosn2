# Generated by Django 3.1.2 on 2020-10-31 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20201023_1708'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_volunteer',
            new_name='is_premier_emp',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='is_employee',
            new_name='is_secondary_emp',
        ),
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'مدير المؤسسه'), (2, 'مشرف جمعيه رئيسيه'), (3, 'مشرف جمعيه تنمويه')], help_text='User Role in A system ', null=True, verbose_name='User Type'),
        ),
    ]
