# Generated by Django 3.1.2 on 2020-10-23 15:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Needy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True, verbose_name='اسم الحاله')),
                ('address', models.CharField(max_length=255, null=True, verbose_name='العنوان')),
                ('national_id', models.CharField(max_length=255, null=True, verbose_name='الرقم القومى')),
                ('phone', models.CharField(max_length=255, null=True, verbose_name='الجوال')),
                ('description', models.CharField(max_length=255, null=True, verbose_name='وصف الحاله')),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case_type', models.SmallIntegerField(choices=[(1, 'عاجله'), (2, 'متوسطه'), (3, 'عاديه')], default=3)),
                ('need_type', models.SmallIntegerField(choices=[(1, 'مال'), (1, 'ملبس'), (1, 'مواد غذائيه')], default=1)),
                ('needy_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='office.needy')),
            ],
        ),
        migrations.CreateModel(
            name='Foundation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True, verbose_name='اسم الحاله')),
                ('address', models.CharField(max_length=255, null=True, verbose_name='العنوان')),
                ('phone', models.CharField(max_length=255, null=True, verbose_name='الجوال')),
                ('description', models.CharField(max_length=255, null=True, verbose_name='وصف الحاله')),
                ('cases', models.ManyToManyField(related_name='case', to='office.Needy', verbose_name='الحالات')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee', to=settings.AUTH_USER_MODEL, verbose_name='مشرفيين')),
            ],
        ),
    ]
