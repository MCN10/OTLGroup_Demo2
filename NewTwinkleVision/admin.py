from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(newTwinkleVisionCsv)
admin.site.register(newTwinkleVisionCustomer)
admin.site.register(newTwinkleVisionProduct)
admin.site.register(newTwinkleVisionCategory)
admin.site.register(newTwinkleVisionOrder)
admin.site.register(newTwinkleVisionOrderItem)
admin.site.register(newTwinkleVisionShippingAddress)
