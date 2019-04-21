from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django import forms
from django.shortcuts import render,redirect 
from django.db import transaction
from django.forms.utils import ValidationError
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Pmodel,CustomUser,Pcompany,Gender,images,interest
from star_ratings.models import Rating
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.core.mail import send_mail
from .tokens import account_activation_token
from django.urls import reverse
from django.contrib.sites.models import Site

class ModelSignUpForm(UserCreationForm):
	username=forms.CharField(min_length=6,max_length=30, required=True, help_text='Username must be 6 letters or more')
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
		username= self.cleaned_data['username']
		if username and Pmodel.objects.filter(user__username__iexact=username).exists():
			self.add_error('username', 'A user with that username already exists.')
		else:
			user.is_model = True
			user.first_name=self.cleaned_data['first_name']
			user.last_name=self.cleaned_data['last_name']
			user.email=self.cleaned_data['email']
			user.is_active = False
			user.save()
			mail_subject = 'Activate Your Account'
			current_site = Site.objects.get_current()
			message = render_to_string('account/acc_active_email.html', {            
				'user': user,
				'domain': current_site.domain,
				'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
				'token':account_activation_token.make_token(user),
			})
			to_email = [
			self.cleaned_data.get('email'),
			]
			# msg_plain = render_to_string('templates/email.txt', {'some_params': some_params})
			msg_html = render_to_string('account/acc_active_email.html', {            
				'user': user,
				'domain': current_site.domain,
				'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
				'token':account_activation_token.make_token(user),
			})

			send_mail(mail_subject, message, 'temidire@phodel.com.ng', to_email, fail_silently=False, html_message=msg_html, )
			pmodel = Pmodel.objects.create(user=user, 
				email=self.cleaned_data.get('email'), 
				gender=self.cleaned_data.get('gender'), 
				first_name=self.cleaned_data.get('first_name'),
				last_name=self.cleaned_data.get('last_name'),
				)
			if pmodel:
				rate = Rating.objects.create(object_id=pmodel.user.pk)
		# pmodel.email.create(*self.cleaned_data.get('email'))
		# pmodel.gender.create(*self.cleaned_data.get('gender'))
		return User

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
