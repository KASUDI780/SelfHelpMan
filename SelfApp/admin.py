

# api/admin.py
from django.contrib import admin
from .models import Member, Contribution, MPesaPayment, SMSLog
# Register your models here.

admin.site.register(Member)
admin.site.register(Contribution)
admin.site.register(MPesaPayment)
admin.site.register(SMSLog)