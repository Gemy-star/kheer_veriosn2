# Generated by Django 3.0.7 on 2020-12-09 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0002_courses_depend_child'),
    ]

    operations = [
        migrations.AddField(
            model_name='needy',
            name='total_donations',
            field=models.IntegerField(default=0, null=True, verbose_name='إجمالى التبرعات'),
        ),
    ]
