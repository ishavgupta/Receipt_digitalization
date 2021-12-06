# forms.py
from django import forms
from .models import *

class BillForm(forms.ModelForm):

	class Meta:
		model = Bill
		fields = ['username','Shop_name','Shop_address', 'Telephone_no','Total_items' ,'Bill_amount', 'Bill_picture']
