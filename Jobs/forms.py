from django import forms
from .models import Job,Lga

class JobModelForm(forms.ModelForm):
	class Meta:
		model= Job
		fields=[
		'Job_title',
		'Job_author',
		'state',
		'lga',
		'town',
		'gender',
		'height',
		'Job_Description',
		'personal_note',
		'street_address',
		]
		widgets={
			'Job_author':forms.HiddenInput()
			}
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['lga'].queryset = Lga.objects.all()