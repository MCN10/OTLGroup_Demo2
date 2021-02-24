import django_filters
from .models import *



class OrderFilter(django_filters.FilterSet):
	class Meta:
		model = opticTradeLinksOrder
		fields = '__all__'
		exclude = ['customer', 'date_created']

class ProductFilter(django_filters.FilterSet):
	class Meta:
		model = opticTradeLinksProduct
		fields = ['name', 'category']

class CategoryFilter(django_filters.FilterSet):
	class Meta:
		model = opticTradeLinksCategory
		fields = ['category_name']
