from django.forms import ModelForm
from .models import *


class CsvModelsForm(ModelForm):
    class Meta:
        model = opticalSparesCsv
        fields = ('file_name',)

class OrderForm(ModelForm):
	class Meta:
		model = opticalSparesOrder
		fields = '__all__'
		exclude = ['customer', 'transaction_id']


class OrderItemsForm(ModelForm):
	class Meta:
		model = opticalSparesOrderItem
		fields = '__all__'


class ShippingDetailsForm(ModelForm):
	class Meta:
		model = opticalSparesShippingAddress
		fields = '__all__'


class ProductsForm(ModelForm):
	class Meta:
		model = opticalSparesProduct
		fields = '__all__'


class CategoriesForm(ModelForm):
	class Meta:
		model = opticalSparesCategory
		fields = '__all__'
		exclude = ['slug']

class Categories2Form(ModelForm):
	class Meta:
		model = opticalSparesCategoryLayer2
		fields = '__all__'
		exclude = ['slug']

class Categories3Form(ModelForm):
	class Meta:
		model = opticalSparesCategoryLayer3
		fields = '__all__'
		exclude = ['slug']

class Categories4Form(ModelForm):
	class Meta:
		model = opticalSparesCategoryLayer4
		fields = '__all__'
		exclude = ['slug']

class Categories5Form(ModelForm):
	class Meta:
		model = opticalSparesCategoryLayer5
		fields = '__all__'
		exclude = ['slug']

class Categories6Form(ModelForm):
	class Meta:
		model = opticalSparesCategoryLayer6
		fields = '__all__'
		exclude = ['slug']
