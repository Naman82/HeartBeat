from django.contrib import admin
from .models import BloodBankProfile,BloodStock,CustomerProfile,DeliveryPersonProfile,User
# Register your models here.

admin.site.register(User)
admin.site.register(BloodBankProfile)
admin.site.register(BloodStock)
admin.site.register(CustomerProfile)
admin.site.register(DeliveryPersonProfile)