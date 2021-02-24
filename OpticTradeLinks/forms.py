from django.forms import ModelForm
from .models import *


class CsvModelsForm(ModelForm):
    class Meta:
        model = opticTradeLinksCsv
        fields = ('file_name',)

class OrderForm(ModelForm):
	class Meta:
		model = opticTradeLinksOrder
		fields = '__all__'
		exclude = ['customer', 'transaction_id']


class OrderItemsForm(ModelForm):
	class Meta:
		model = opticTradeLinksOrderItem
		fields = '__all__'


class ShippingDetailsForm(ModelForm):
	class Meta:
		model = opticTradeLinksShippingAddress
		fields = '__all__'


class ProductsForm(ModelForm):
	class Meta:
		model = opticTradeLinksProduct
		fields = '__all__'


class CategoriesForm(ModelForm):
	class Meta:
		model = opticTradeLinksCategory
		fields = '__all__'
		exclude = ['slug']

class Categories2Form(ModelForm):
	class Meta:
		model = opticTradeLinksCategoryLayer2
		fields = '__all__'
		exclude = ['slug']

class Categories3Form(ModelForm):
	class Meta:
		model = opticTradeLinksCategoryLayer3
		fields = '__all__'
		exclude = ['slug']

class Categories4Form(ModelForm):
	class Meta:
		model = opticTradeLinksCategoryLayer4
		fields = '__all__'
		exclude = ['slug']

class Categories5Form(ModelForm):
	class Meta:
		model = opticTradeLinksCategoryLayer5
		fields = '__all__'
		exclude = ['slug']

class Categories6Form(ModelForm):
	class Meta:
		model = opticTradeLinksCategoryLayer6
		fields = '__all__'
		exclude = ['slug']
