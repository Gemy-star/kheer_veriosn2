from django.db import models
from accounts.models import User


class Needy(models.Model):
    name = models.CharField(max_length=255, null=True, verbose_name='اسم الحاله')
    address = models.CharField(max_length=255, null=True, verbose_name='العنوان')
    national_id = models.CharField(max_length=255, null=True, verbose_name='الرقم القومى')
    phone = models.CharField(max_length=255, null=True, verbose_name='الجوال')
    description = models.CharField(max_length=255, null=True, verbose_name='وصف الحاله')

    def __str__(self):
        return self.name


class Foundation(models.Model):
    name = models.CharField(max_length=255, null=True, verbose_name='اسم المؤسسه')
    address = models.CharField(max_length=255, null=True, verbose_name='العنوان')
    phone = models.CharField(max_length=255, null=True, verbose_name='الجوال')
    description = models.CharField(max_length=255, null=True, verbose_name='عن المؤسسه')
    cases = models.ManyToManyField(Needy, related_name='case', verbose_name='الحالات')
    employee = models.ManyToManyField(User, related_name='employee', verbose_name='مشرفيين')

    def __str__(self):
        return self.name


class Status(models.Model):
    needy_status = models.ForeignKey(Needy, on_delete=models.CASCADE)
    CASE_TYPE = [
        (1, 'عاجله'),
        (2, 'متوسطه'),
        (3, 'عاديه'),

    ]
    case_type = models.SmallIntegerField(default=3, choices=CASE_TYPE)
    NEED_TYPE = [
        (1, 'مال'),
        (1, 'ملبس'),
        (1, 'مواد غذائيه'),

    ]
    need_type = models.SmallIntegerField(default=1, choices=NEED_TYPE)

    def __str__(self):
        return '{} {}'.format('حالة', self.needy_status.name)
