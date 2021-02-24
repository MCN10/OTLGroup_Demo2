from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(opticalLensLabCsv)
admin.site.register(opticalLensLabCustomer)
admin.site.register(opticalLensLabProduct)
admin.site.register(opticalLensLabCategory)
admin.site.register(opticalLensLabOrder)
admin.site.register(opticalLensLabOrderItem)
admin.site.register(opticalLensLabShippingAddress)
