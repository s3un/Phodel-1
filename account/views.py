from django.shortcuts import render
from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView, TemplateView
from .forms import ModelSignUpForm, CompanySignUpForm
from .models import CustomUser
# Create your views here.

class SignUpView(TemplateView):
	template_name = 'account/signup.html'


class ModelSignUpView(CreateView):
	model= CustomUser
	form_class=ModelSignUpForm
	template_name= 'account/signup_form.html'

	def get_context_data(self, **kwargs):
		kwargs['user_type'] = 'Model'
		return super().get_context_data(**kwargs)

	def form_valid(self, form):
		user = form.save()
		login(self.request, user)
		return redirect('Home:index')


class CompanySignUpView(CreateView):
	model = CustomUser
	form_class = CompanySignUpForm
	template_name = 'account/signup_form.html'

	def get_context_data(self, **kwargs):
		kwargs['user_type'] = 'Seeker'
		return super().get_context_data(**kwargs)

	def form_valid(self, form):
		user = form.save()
		login(self.request, user)
		return redirect('Home:index')
