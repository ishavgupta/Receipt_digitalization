# forms.py
from django import forms
from .models import *

class BillForm(forms.ModelForm):

	class Meta:
		model = Bill
		fields = ['username','Shop_name','Bill_picture']
