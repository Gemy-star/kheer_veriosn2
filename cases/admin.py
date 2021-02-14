from django.contrib import admin
from .models import TamkeenPayment, Contact, Payment, Certificate, TamkeenSupply, VolunteerProfile, TechnicalSupport

admin.site.register(Contact)
admin.site.register(Payment)
admin.site.register(Certificate)
admin.site.register(TamkeenSupply)
admin.site.register(VolunteerProfile)
admin.site.register(TechnicalSupport)
admin.site.register(TamkeenPayment)
