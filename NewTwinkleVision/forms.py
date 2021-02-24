from django.forms import ModelForm
from .models import *


class CsvModelsForm(ModelForm):
    class Meta:
        model = newTwinkleVisionCsv
        fields = ('file_name',)

class OrderForm(ModelForm):
	class Meta:
		model = newTwinkleVisionOrder
		fields = '__all__'
		exclude = ['customer', 'transaction_id']


class OrderItemsForm(ModelForm):
	class Meta:
		model = newTwinkleVisionOrderItem
		fields = '__all__'


class ShippingDetailsForm(ModelForm):
	class Meta:
		model = newTwinkleVisionShippingAddress
		fields = '__all__'


class ProductsForm(ModelForm):
	class Meta:
		model = newTwinkleVisionProduct
		fields = '__all__'


class CategoriesForm(ModelForm):
	class Meta:
		model = newTwinkleVisionCategory
		fields = '__all__'
		exclude = ['slug']

class Categories2Form(ModelForm):
	class Meta:
		model = newTwinkleVisionCategoryLayer2
		fields = '__all__'
		exclude = ['slug']

class Categories3Form(ModelForm):
	class Meta:
		model = newTwinkleVisionCategoryLayer3
		fields = '__all__'
		exclude = ['slug']

class Categories4Form(ModelForm):
	class Meta:
		model = newTwinkleVisionCategoryLayer4
		fields = '__all__'
		exclude = ['slug']

class Categories5Form(ModelForm):
	class Meta:
		model = newTwinkleVisionCategoryLayer5
		fields = '__all__'
		exclude = ['slug']

class Categories6Form(ModelForm):
	class Meta:
		model = newTwinkleVisionCategoryLayer6
		fields = '__all__'
		exclude = ['slug']
