from django.forms import ModelForm
from .models import *


class CsvModelsForm(ModelForm):
    class Meta:
        model = opticalLensLabCsv
        fields = ('file_name',)

class OrderForm(ModelForm):
	class Meta:
		model = opticalLensLabOrder
		fields = '__all__'
		exclude = ['customer', 'transaction_id']


class OrderItemsForm(ModelForm):
	class Meta:
		model = opticalLensLabOrderItem
		fields = '__all__'


class ShippingDetailsForm(ModelForm):
	class Meta:
		model = opticalLensLabShippingAddress
		fields = '__all__'


class ProductsForm(ModelForm):
	class Meta:
		model = opticalLensLabProduct
		fields = '__all__'


class CategoriesForm(ModelForm):
	class Meta:
		model = opticalLensLabCategory
		fields = '__all__'
		exclude = ['slug']

class Categories2Form(ModelForm):
	class Meta:
		model = opticalLensLabCategoryLayer2
		fields = '__all__'
		exclude = ['slug']

class Categories3Form(ModelForm):
	class Meta:
		model = opticalLensLabCategoryLayer3
		fields = '__all__'
		exclude = ['slug']

class Categories4Form(ModelForm):
	class Meta:
		model = opticalLensLabCategoryLayer4
		fields = '__all__'
		exclude = ['slug']

class Categories5Form(ModelForm):
	class Meta:
		model = opticalLensLabCategoryLayer5
		fields = '__all__'
		exclude = ['slug']

class Categories6Form(ModelForm):
	class Meta:
		model = opticalLensLabCategoryLayer6
		fields = '__all__'
		exclude = ['slug']
