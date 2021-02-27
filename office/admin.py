from django.contrib import admin
from . import models
# Register your models here.


admin.site.register(models.Foundation)
admin.site.register(models.Needy)
admin.site.register(models.Dependency)
admin.site.register(models.Provider)
admin.site.register(models.Courses)
admin.site.register(models.CourseBag)
admin.site.register(models.PaymentCourseBag)
admin.site.register(models.BagCertificate)
admin.site.register(models.PayTicket)
admin.site.register(models.GreenParticipant)
admin.site.register(models.PayDonation)
