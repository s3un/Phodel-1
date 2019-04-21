from django import forms
from .models import comment
# from django.contrib.flatpages.models import FlatPage
from tinymce.widgets import TinyMCE

class myComment(forms.ModelForm):
	class Meta:
		model = comment
		fields = ['Name', 'Comment','News_Id']
		widgets={
			'News_Id':forms.HiddenInput(),
			'Comment':TinyMCE(attrs={'cols': 80, 'rows': 10})
		}
	
			
	
		