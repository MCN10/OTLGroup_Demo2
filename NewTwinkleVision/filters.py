import django_filters
from .models import *



class OrderFilter(django_filters.FilterSet):
	class Meta:
		model = newTwinkleVisionOrder
		fields = '__all__'
		exclude = ['customer', 'date_created']

class ProductFilter(django_filters.FilterSet):
	class Meta:
		model = newTwinkleVisionProduct
		fields = ['name', 'category']

class CategoryFilter(django_filters.FilterSet):
	class Meta:
		model = newTwinkleVisionCategory
		fields = ['category_name']
