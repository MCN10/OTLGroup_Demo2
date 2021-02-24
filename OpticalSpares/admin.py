from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(opticalSparesCsv)
admin.site.register(opticalSparesCustomer)
admin.site.register(opticalSparesProduct)
admin.site.register(opticalSparesCategory)
admin.site.register(opticalSparesOrder)
admin.site.register(opticalSparesOrderItem)
admin.site.register(opticalSparesShippingAddress)
