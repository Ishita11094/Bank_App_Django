from django import forms
from .models import CreateModel, TransactionModel

class CreateForm(forms.ModelForm):
	class Meta:
		model = CreateModel
		fields = '__all__'

class TransactionForm(forms.ModelForm):
	class Meta:
		model = TransactionModel
		fields = '__all__'


