from django.forms import ModelForm
from .models import *


class CsvModelsForm(ModelForm):
    class Meta:
        model = houseOfBrandsCsv
        fields = ('file_name',)

class OrderForm(ModelForm):
	class Meta:
		model = houseOfBrandsOrder
		fields = '__all__'
		exclude = ['customer', 'transaction_id']


class OrderItemsForm(ModelForm):
	class Meta:
		model = houseOfBrandsOrderItem
		fields = '__all__'


class ShippingDetailsForm(ModelForm):
	class Meta:
		model = houseOfBrandsShippingAddress
		fields = '__all__'


class ProductsForm(ModelForm):
	class Meta:
		model = houseOfBrandsProduct
		fields = '__all__'


class CategoriesForm(ModelForm):
	class Meta:
		model = houseOfBrandsCategory
		fields = '__all__'
		exclude = ['slug']

class Categories2Form(ModelForm):
	class Meta:
		model = houseOfBrandsCategoryLayer2
		fields = '__all__'
		exclude = ['slug']

class Categories3Form(ModelForm):
	class Meta:
		model = houseOfBrandsCategoryLayer3
		fields = '__all__'
		exclude = ['slug']

class Categories4Form(ModelForm):
	class Meta:
		model = houseOfBrandsCategoryLayer4
		fields = '__all__'
		exclude = ['slug']

class Categories5Form(ModelForm):
	class Meta:
		model = houseOfBrandsCategoryLayer5
		fields = '__all__'
		exclude = ['slug']

class Categories6Form(ModelForm):
	class Meta:
		model = houseOfBrandsCategoryLayer6
		fields = '__all__'
		exclude = ['slug']
