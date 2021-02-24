import django_filters
from .models import *



class OrderFilter(django_filters.FilterSet):
	class Meta:
		model = houseOfBrandsOrder
		fields = '__all__'
		exclude = ['customer', 'date_created']

class ProductFilter(django_filters.FilterSet):
	class Meta:
		model = houseOfBrandsProduct
		fields = ['name', 'category']

class CategoryFilter(django_filters.FilterSet):
	class Meta:
		model = houseOfBrandsCategory
		fields = ['category_name']
