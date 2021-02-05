from django.db import models
from accounts.models import User
from datetime import date
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
    name = models.CharField(null=True, max_length=255, verbose_name='الأسم')

    def __str__(self):
        return self.name


class Needy(models.Model):
    name = models.CharField(max_length=255, null=True, verbose_name='اسم الحاله')
    HOME_CHOICES = (
        ('ملك', 'ملك'),
        ('إيجار', 'إيجار'),
        ('أخرى', 'أخرى'),

    )
    home = models.CharField(null=True, max_length=255, choices=HOME_CHOICES, verbose_name='السكن')
    national_id = models.CharField(unique=True, max_length=255, null=True, verbose_name='رقم الهويه')
    phone = models.CharField(max_length=255, null=True, verbose_name='الجوال')
    parent = models.CharField(max_length=255, null=True, verbose_name='العائل')
    job = models.CharField(max_length=255, null=True, verbose_name='المهنه')

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
    amount = models.IntegerField(null=True, max_length=255, verbose_name='قيمة الدعم')
    total_donations = models.IntegerField(null=True, default=0, verbose_name='إجمالى التبرعات')

    def __str__(self):
        return self.name


class Foundation(models.Model):
    name = models.CharField(max_length=255, null=True, verbose_name='اسم المؤسسه')
    address = models.CharField(max_length=255, null=True, verbose_name='العنوان')
    phone = models.CharField(max_length=255, null=True, verbose_name='الجوال')
    description = models.CharField(max_length=255, null=True, verbose_name='عن المؤسسه')
    cases = models.ManyToManyField(Needy, related_name='case', verbose_name='الحالات', null=True)
    employee = models.ManyToManyField(User, related_name='employee', null=True, verbose_name='مشرفيين')

    def __str__(self):
        return self.name


class Provider(models.Model):
    name = models.CharField(max_length=255, null=True, verbose_name='اسم الراعى')
    address = models.CharField(max_length=255, null=True, verbose_name='العنوان')
    phone = models.CharField(max_length=255, null=True, verbose_name='الجوال')
    description = models.CharField(max_length=255, null=True, verbose_name='عن المؤسسه')
    employee = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Courses(models.Model):
    name = models.CharField(max_length=255, null=True, verbose_name='اسم الدوره')
    description = models.CharField(max_length=255, null=True, verbose_name='عن الدوره')
    provider = models.ForeignKey(Provider, null=True, on_delete=models.CASCADE, verbose_name='الراعى')
    start_date = models.DateField(verbose_name="تاريخ البدايه",null=True, auto_now=False, auto_now_add=False)
    end_date = models.DateField(verbose_name="تاريخ النهايه", null=True,auto_now=False, auto_now_add=False ,)
    @property
    def is_past_due(self):
            return date.today() > self.end_date

    def __str__(self):
        return self.name




class GreenParticipant(models.Model):
    participant = models.OneToOneField(User ,on_delete=models.CASCADE , verbose_name='المشارك')
    foundation = models.ForeignKey(Foundation , on_delete=models.CASCADE , verbose_name='المؤسسه')
    provider = models.ForeignKey(Provider , blank=True , null=True,on_delete=models.CASCADE , verbose_name='الداعم')
    date_added = models.DateTimeField(auto_now_add=True , verbose_name='تاريخ اﻷضافه')
    def __str__(self):
        return self.foundation.name
        

class CourseBag(models.Model):
    name = models.CharField(max_length=255, null=True, verbose_name='اسم الدوره')
    description = models.CharField(max_length=255, null=True, verbose_name='عن الدوره')
    link = models.URLField(
        verbose_name='المسار',
        max_length=128,
        db_index=True,
        unique=True,
        blank=True,
        null=True
    )
    start_date = models.DateField(verbose_name="تاريخ البدايه",null=True, auto_now=False, auto_now_add=False)
    end_date = models.DateField(verbose_name="تاريخ النهايه", null=True,auto_now=False, auto_now_add=False ,)
    total_hours = models.IntegerField(null=True , blank=True , verbose_name='عدد الساعات')
    trainer = models.ForeignKey(User , on_delete=models.CASCADE , verbose_name='المدرب')
    green = models.ManyToManyField(GreenParticipant , verbose_name='المشاركين' ,null=True , blank=True)
    foundation = models.ForeignKey(Foundation ,null=True, blank=True, on_delete=models.CASCADE , verbose_name='المؤسسه')
    @property
    def is_past_due(self):
            return date.today() > self.end_date
    def __str__(self):
        return self.name
class PaymentCourseBag(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='المستخدم')
    course = models.ForeignKey(CourseBag, on_delete=models.CASCADE, verbose_name='الحقيبه')
    needy = models.ForeignKey(Needy, on_delete=models.CASCADE, verbose_name='المستفيد')

    def __str__(self):
        return self.user.first_name


class PayTicket(models.Model):
    needy = models.OneToOneField(Needy, on_delete=models.CASCADE, verbose_name='المستفيد')
    ticket = models.FileField(verbose_name='سند الصرف', null=True, blank=True)

    def __str__(self):
        return self.needy.name


class BagCertificate(models.Model):
    bag = models.ForeignKey(Courses, on_delete=models.CASCADE, null=True, verbose_name='الحقيبه')
    needy = models.ForeignKey(Needy, on_delete=models.CASCADE, null=True, verbose_name='المستفيد')
    certificate = models.FileField(null=True, blank=True, verbose_name='الشهاده')

    def __str__(self):
        return self.needy.name
