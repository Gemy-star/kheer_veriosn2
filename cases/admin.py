from django.contrib import admin
from .models import NeedyCase, Contact , Payment , Certificate


admin.site.register(NeedyCase)
admin.site.register(Contact)
admin.site.register(Payment)
admin.site.register(Certificate)
