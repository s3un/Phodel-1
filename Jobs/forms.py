from django import forms
from .models import Job

class JobModelForm(forms.ModelForm):
	class Meta:
		model= Job
		fields=[
		'Job_title',
		'state',
		'lga',
		'town',
		'gender',
		'height',
		'Job_Description',
		'personal_note',
		'street_address',
		]