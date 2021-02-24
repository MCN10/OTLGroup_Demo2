from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(opticTradeLinksCsv)
admin.site.register(opticTradeLinksCustomer)
admin.site.register(opticTradeLinksProduct)
admin.site.register(opticTradeLinksCategory)
admin.site.register(opticTradeLinksOrder)
admin.site.register(opticTradeLinksOrderItem)
admin.site.register(opticTradeLinksShippingAddress)
