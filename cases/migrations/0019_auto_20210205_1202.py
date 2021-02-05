# Generated by Django 3.1.5 on 2021-02-05 12:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('office', '0017_coursebag_foundation'),
        ('cases', '0018_auto_20210119_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tamkeensupply',
            name='tamkeen_type',
            field=models.SmallIntegerField(blank=True, choices=[(1, 'تمكين منتهى بمقابل مادى'), (2, 'تمكين منتهى بفرصة عمل'), (3, 'غير مرشح')], null=True),
        ),
        migrations.CreateModel(
            name='TamkeenPayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cases.tamkeensupply')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TamkeenCourses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tamkeen', models.SmallIntegerField(blank=True, choices=[(1, 'تمكين منتهى بمقابل مادى'), (2, 'تمكين منتهى بفرصة عمل')], null=True)),
                ('courses', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='office.courses')),
            ],
        ),
    ]
