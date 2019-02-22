from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django import forms
from django.db import transaction
from django.forms.utils import ValidationError
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Pmodel,CustomUser,Pcompany,Gender,images,interest
class ModelSignUpForm(UserCreationForm):
	first_name = forms.CharField(max_length=30, required=True, help_text='Enter your Firstname')
	last_name = forms.CharField(max_length=30, required=True, help_text='Enter your Lastname')
	email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
	gender = forms.ModelChoiceField(queryset=Gender.objects.all(), )
	class Meta(UserCreationForm.Meta):
		# User= get_user_model()
		model = CustomUser
		fields= ('username', 'first_name', 'last_name','gender', 'email', 'password1', 'password2' )
	def save(self):
		user = super().save(commit=False)
		user.is_model = True
		user.first_name=self.cleaned_data['first_name']
		user.last_name=self.cleaned_data['last_name']
		user.email=self.cleaned_data['email']
		user.save()
		pmodel = Pmodel.objects.create(user=user, 
			email=self.cleaned_data.get('email'), 
			gender=self.cleaned_data.get('gender'), 
			first_name=self.cleaned_data.get('first_name'),
			last_name=self.cleaned_data.get('last_name')
			)
		# pmodel.email.create(*self.cleaned_data.get('email'))
		# pmodel.gender.create(*self.cleaned_data.get('gender'))
		return user

class CompanySignUpForm(UserCreationForm):
	email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
	company_name= forms.CharField()
	class Meta(UserCreationForm.Meta):
		# User= get_user_model()
		model = CustomUser
		help_texts = {
            'password': None,
            'email': None,
        }

	
	def save(self):
		user = super().save(commit=False)
		user.is_company = True
		user.save()
		group = Group.objects.get(name='Company')
		user.groups.add(group)
		pcompany = Pcompany.objects.create(user=user, email=self.cleaned_data.get('email'), company_name=self.cleaned_data.get('company_name'))
		# pcompany.email.create(*self.cleaned_data.get('email'))
		# pcompany.company_name.create(*self.cleaned_data.get('company_name'))
		return user

class register(UserCreationForm):
	email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

	class Meta(UserCreationForm):
		model = CustomUser
		fields = ('username', 'email', 'is_model', 'is_company')

class Change_detail(UserChangeForm):
	email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

	class Meta:
		model = CustomUser
		fields = ('username','email', 'is_model', 'is_company')
class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = images
        fields = ['User',
        		'image',
        		 ]
        widgets={
        'User':forms.HiddenInput()
        }

class InterestForm(forms.ModelForm):
    class Meta:
        model = interest
        fields = ['Users',
        		'interests',
        		 ]
        widgets={
        'Users':forms.HiddenInput()
        }    
