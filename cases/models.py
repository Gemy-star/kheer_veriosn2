from django.db import models
from office.models import Needy, Foundation, Dependency
from accounts.models import User


class NeedyCase(models.Model):
    CASES_CHOICES = (
        (1, 'دعم الكهرباء'),
        (2, 'دعم الغذاء'),
        (3, 'دعم التعليم'),
        (4, 'دعم الماء'),
        (5, 'دعم الملبس'),
    )
    details = models.TextField(blank=True, null=True, verbose_name='عرض الحاله')
    case = models.OneToOneField(Needy, on_delete=models.CASCADE)
    case_type = models.SmallIntegerField(blank=True, choices=CASES_CHOICES, null=True, verbose_name='نوع الحاله')

    def __str__(self):
        return self.case.name


class VolunteerProfile(models.Model):
    job = models.CharField(max_length=255, null=True, blank=True, verbose_name='المهنه')
    desc = models.CharField(max_length=255, null=True, blank=True, verbose_name='التخصص')
    volunteer = models.OneToOneField(User, null=True, verbose_name='المتطوع', on_delete=models.CASCADE)

    def __str__(self):
        return self.volunteer.first_name


class Contact(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True, verbose_name='الأسم')
    address = models.CharField(max_length=255, null=True, blank=True, verbose_name='العنوان')
    phone = models.CharField(max_length=255, null=True, blank=True, verbose_name='الهاتف')
    message = models.TextField(null=True, blank=True, verbose_name='الرساله')

    def __str__(self):
        return self.name


class Payment(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True, verbose_name='الأسم')
    address = models.CharField(max_length=255, null=True, blank=True, verbose_name='العنوان')
    phone = models.CharField(max_length=255, null=True, blank=True, verbose_name='الهاتف')
    national_id = models.CharField(max_length=255, null=True, blank=True, verbose_name='الهويه')
    ammount = models.IntegerField(null=True, blank=True, verbose_name='المبلغ')
    helper = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    case = models.ForeignKey(Needy, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Certificate(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True, verbose_name='اسم الشهاده')
    description = models.TextField(null=True, blank=True, verbose_name='وصف')
    found = models.ForeignKey(Foundation, on_delete=models.CASCADE)
    volunteer = models.ForeignKey(User, on_delete=models.CASCADE)
    paper = models.FileField(upload_to='documents/', null=True)

    def __str__(self):
        return self.name


class HebaKheer(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True, verbose_name='اسم ')
    address = models.CharField(max_length=255, null=True, blank=True, verbose_name='العنوان')
    phone = models.CharField(max_length=255, null=True, blank=True, verbose_name='الهاتف')
    national_id = models.CharField(max_length=255, null=True, blank=True, verbose_name='الهويه')
    ammount = models.IntegerField(null=True, blank=True, verbose_name='المبلغ')

    def __str__(self):
        return self.name


class TamkeenSupply(models.Model):
    case = models.OneToOneField(Needy, on_delete=models.CASCADE, null=True, blank=True)
    depend = models.OneToOneField(Dependency, on_delete=models.CASCADE, null=True, blank=True)
    TAMKEEN_CHOICES = (
        (1, 'تمكين منتهى بتدريب'),
        (2, 'تمكين منتهى بمقابل مادى'),
        (3, 'تمكين منتهى بفرصة عمل')

    )
    tamkeen_type = models.SmallIntegerField(null=True, blank=True, choices=TAMKEEN_CHOICES)

    def __str__(self):
        return str(self.tamkeen_type)
