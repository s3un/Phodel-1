from django.shortcuts import render
from django.contrib.auth import login
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.views.generic.edit import UpdateView
from .forms import ModelSignUpForm, CompanySignUpForm, ImageUploadForm, InterestForm
from .models import CustomUser, Pmodel,Pcompany, images, interest
from django.contrib.auth import get_user_model
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.core.mail import send_mail
from .tokens import account_activation_token
from star_ratings.models import Rating
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
		# login(self.request, user)
		return redirect('Home:verify')

def verify(request):
	template= 'account/send.html'
	return render (request, template)


def activate(request, uidb64, token):
	User=get_user_model()
	try:
		uid = urlsafe_base64_decode(uidb64).decode()
		user = User.objects.get(pk=uid)
	except(TypeError, ValueError, OverflowError, User.DoesNotExist):
		user = None
	if user is not None and account_activation_token.check_token(user, token):
		user.is_active = True
		user.save()
		profil = CustomUser.objects.get(pk=uid)
		info = Pmodel.objects.get(user__pk=profil.pk)
		Rating.objects.create(object_id=info.pk)
		# login(request, user)
		return redirect('Home:login')
		return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
	else:
		return HttpResponse('Activation link is invalid!')

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

class add_image(CreateView):
	form_class= ImageUploadForm
	template_name='account/image_upload.html'

	def get(self,request):
		form=self.form_class(None)
		profil = CustomUser.objects.get(pk=request.user.pk)
		info = Pmodel.objects.get(user__pk=profil.pk)
		context={
		'form':form,
		'info':info,
		}
		return render(request, self.template_name, context)

	def post(self,request, **kwargs):
		form=self.form_class(request.POST,  request.FILES)
		if form.is_valid():
			create=form.save(commit=False)
			c= form.cleaned_data
			User=c['User'],
			image=c['image']
			create.save()
			return redirect('Home:profile')

def Remove_image(request, pk):
	img= images.objects.get(pk=pk).delete()
	return redirect('Home:profile')

class add_interest(CreateView):
	form_class= InterestForm
	template_name='account/interest_add.html'

	def get(self,request):
		form=self.form_class(None)
		profil = CustomUser.objects.get(pk=request.user.pk)
		info = Pmodel.objects.get(user__pk=profil.pk)
		context={
		'form':form,
		'info':info,
		}
		return render(request, self.template_name, context)

	def post(self,request, **kwargs):
		form=self.form_class(request.POST,  request.FILES)
		if form.is_valid():
			create=form.save(commit=False)
			c= form.cleaned_data
			Users=c['Users'],
			interests=c['interests']
			create.save()
			return redirect('Home:profile')

def Remove_interest(request, pk):
	intr= interest.objects.get(pk=pk).delete()
	return redirect('Home:profile')

class Career(UpdateView):
	model=Pmodel
	fields = ['career_summary']
	template_name = 'account/Pmodel_update_form.html'
	success_url= reverse_lazy('Home:profile')

class Statistics(UpdateView):
	model=Pmodel
	fields = ['height','age','weight','skin_color']
	template_name = 'account/Pmodel_update_form.html'
	success_url= reverse_lazy('Home:profile')

class ImageUpdate(UpdateView):
	model=Pmodel
	fields = ['last_name','first_name','model_image']
	template_name = 'account/Pmodel_update_form.html'
	success_url= reverse_lazy('Home:profile')