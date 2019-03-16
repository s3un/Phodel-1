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
		'payout',
		'Job_Description',
		'personal_note',
		'street_address',
		]
		widgets={
			'Job_author':forms.HiddenInput(),
			'gender':forms.CheckboxSelectMultiple(),
			}
		help_texts={
			'payout':'Enter Payment for gig',
			'height':'Enter required height in Feet',
			'Job_title':'Enter Gig Title',
			'state':'Select State of the gig',
			'lga':'Select lga of the gig',
			'Job_Description':'Enter Gig Description',
			'street_address':'Enter street address of the gig',
			'town':'Enter town of the Gig',

		}
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['lga'].queryset = Lga.objects.all()