import django_filters
from .models import *



class OrderFilter(django_filters.FilterSet):
	class Meta:
		model = opticalLensLabOrder
		fields = '__all__'
		exclude = ['customer', 'date_created']

class ProductFilter(django_filters.FilterSet):
	class Meta:
		model = opticalLensLabProduct
		fields = ['name', 'category']

class CategoryFilter(django_filters.FilterSet):
	class Meta:
		model = opticalLensLabCategory
		fields = ['category_name']
