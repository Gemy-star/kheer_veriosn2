from django.db import models
from accounts.models import User


class Dependency(models.Model):
    GENDER_CHOICES = (
        ('M', 'ذكر'),
        ('F', 'أنثى'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name='النوع')
    STAGE_CHOICES = (
        ('التمهيدى', 'التمهيدى'),
        ('الأبتدائى', 'الأبتدائى'),
        ('الأعدادى', 'الأعدادى'),
        ('الثانوى', 'الثانوى'),
        ('الجامعه', 'الجامعه'),
    )
    stage = models.CharField(max_length=255, choices=STAGE_CHOICES, verbose_name='المرحله')
    age = models.SmallIntegerField(null=True, verbose_name='العمر')

    def __str__(self):
        return str(self.gender)


class Needy(models.Model):
    name = models.CharField(max_length=255, null=True, verbose_name='اسم الحاله')
    HOME_CHOICES = (
        ('ملك', 'ملك'),
        ('إيجار', 'إيجار'),
        ('أخرى', 'أخرى'),

    )
    home = models.CharField(null=True, max_length=255, choices=HOME_CHOICES, verbose_name='السكن')
    national_id = models.CharField(max_length=255, null=True, verbose_name='رقم الهويه')
    phone = models.CharField(max_length=255, null=True, verbose_name='الجوال')
    parent = models.CharField(max_length=255, null=True, verbose_name='العائل')

    SOURCE_CHOICES = (
        ('راتب شهري', 'راتب شهري'),
        ('ضمان اجتماعي', 'ضمان اجتماعي'),
        ('حساب مواطن', 'حساب مواطن'),
        ('اخرى ', 'اخرى '),

    )
    source_income = models.CharField(null=True, max_length=255, choices=SOURCE_CHOICES, verbose_name='مصدر الدخل')
    dependencies = models.ManyToManyField(Dependency, verbose_name='الاطفال')
    HEALTH_STATUS = (
        ('مريض', 'مريض'), ('حالة حرجة', 'حالة حرجة'), ('صحة جيدة', 'صحة جيدة'),
    )
    health_status = models.CharField(null=True, max_length=255, choices=HEALTH_STATUS, verbose_name='الحاله الصحيه')
    status = models.CharField(max_length=255, null=True, blank=True, verbose_name='الحالة الاجتماعية')
    age = models.SmallIntegerField(null=True, verbose_name='العمر')
    data_added = models.DateField(auto_now_add=True, null=True)
    case_number = models.SmallIntegerField(null=True, blank=True)
    emp_name = models.CharField(null=True, max_length=255, verbose_name='اسم المشرف')
    support = models.CharField(null=True, max_length=255, verbose_name='الدعم المقدم')
    department = models.CharField(null=True, max_length=255, verbose_name='المنطقة')
    amount = models.CharField(null=True, max_length=255, verbose_name='قيمة الدعم')

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


