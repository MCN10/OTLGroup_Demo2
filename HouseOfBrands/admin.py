from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(houseOfBrandsCsv)
admin.site.register(houseOfBrandsCustomer)
admin.site.register(houseOfBrandsProduct)
admin.site.register(houseOfBrandsCategory)
admin.site.register(houseOfBrandsOrder)
admin.site.register(houseOfBrandsOrderItem)
admin.site.register(houseOfBrandsShippingAddress)
