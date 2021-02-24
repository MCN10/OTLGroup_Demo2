import django_filters
from .models import *



class OrderFilter(django_filters.FilterSet):
	class Meta:
		model = opticalSparesOrder
		fields = '__all__'
		exclude = ['customer', 'date_created']

class ProductFilter(django_filters.FilterSet):
	class Meta:
		model = opticalSparesProduct
		fields = ['name', 'category']

class CategoryFilter(django_filters.FilterSet):
	class Meta:
		model = opticalSparesCategory
		fields = ['category_name']
