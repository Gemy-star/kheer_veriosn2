# Generated by Django 3.1.4 on 2020-12-24 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0005_auto_20201212_1927'),
        ('cases', '0009_hebakheer'),
    ]

    operations = [
        migrations.CreateModel(
            name='TamkeenSupply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tamkeen_type', models.SmallIntegerField(blank=True, choices=[(1, 'تمكين منتهى بتدريب'), (2, 'تمكين منتهى بمقابل مادى'), (3, 'تمكين منتهى بمقايل مادى')], null=True)),
                ('case', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='office.needy')),
                ('depend', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='office.dependency')),
            ],
        ),
    ]