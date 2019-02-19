from django.shortcuts import render, get_object_or_404,redirect
from django.views import generic
from .models import Phodel
from Jobs.models import Job, Hot_Jobs, Featured_Jobs, Application
from django.contrib.auth.decorators import login_required
from Jobs.forms import JobModelForm
from account.models import Pmodel, Pcompany,CustomUser,images,interest
from django.db.models import Q
# Create your views here.
def Home(request):
		template= 'home/index.html'
		phodel = Phodel.objects.all()
		context = {
		# 'category': category,
		'phodel':phodel,
		
		}
		return render(request, template, context)
def base(request):
	if request.user.is_model==True:
		template= 'home/base.html'
		phodel = Phodel.objects.all()
		profi = CustomUser.objects.get(pk=request.user.pk)
		pmod = Pmodel.objects.get(user__pk=profi.pk)
		context = {
		# 'category': category,
		'profi':profi,
		'phodel':phodel,
		'pmod':pmod,
		
		}
		return render(request, template, context)
	else:
		template= 'home/base.html'
		phodel = Phodel.objects.all()
		context = {
		# 'category': category,
		'phodel':phodel,

		
		}
		return render(request, template, context)

@login_required
def profile(request, pk):
	if request.user.is_model==True:
		template= 'home/profile.html'
		profi = CustomUser.objects.get(pk=pk)
		info = Pmodel.objects.get(user__pk=profi.pk)
		imge = images.objects.filter(User__pk=info.pk)
		inter=interest.objects.filter(Users__pk=info.pk)
		context = {
		'profi':profi,
		'info':info,
		'imge':imge,
		'inter':inter,
		}
		return render(request, template, context)
	if request.user.is_company==True:
		template= 'home/Company_profile.html'
		profi = CustomUser.objects.get(pk=pk)
		info = Pcompany.objects.get(user__pk=profi.pk)
		context = {
		'profi':profi,
		'info':info,
		}
		return render(request, template, context)
		
def LoginViews(request):
	if request.user.is_model==True:
		template= 'Jobs/jobs.html'
		# category = get_object_or_404(categories, pk=pk)
		profil = CustomUser.objects.get(pk=request.user.pk)
		info = Pmodel.objects.get(user__pk=profil.pk)
		appl= Application.objects.filter(applicant_id=info.pk)
		hjobs= Hot_Jobs.objects.all()
		Fjobs= Featured_Jobs.objects.all()
		job = Job.objects.filter(is_active=True).order_by('-created_date')
		
		context = {
		# 'category': category,
		'hjobs': hjobs,
		'Fjobs':Fjobs,
		'job': job,
		'appl':appl,		
		}
		return render(request, template, context)
	elif request.user.is_company==True:
		return redirect('Home:company')
		# template= 'Jobs/company_home.html'
		# # category = get_object_or_404(categories, pk=pk)
		# hjobs= Hot_Jobs.objects.all()
		# Fjobs= Featured_Jobs.objects.all()
		# form= JobModelForm()
		# if request.method =='POST':
		# 	if form.is_valid():
		# 		c=form.cleaned_data
		# 		create=Job.objects.create(
		# 			Job_title=c['Job_title'],
		# 			state=c['state'],
		# 			lga=c['lga'],
		# 			town =c['town'],
		# 			gender=c['gender'],
		# 			height=c['height'],
		# 			Job_Description=c['Job_Description'],
		# 			personal_note=c['personal_note'],
		# 			street_address=c['street_address'],
		# 			)
				
		# # job = Job.objects.filter(is_active=True).order_by('-created_date')
		# profil = CustomUser.objects.get(pk=request.user.pk)
		# info = Pcompany.objects.get(user__pk=profil.pk)
		# jobs = Job.objects.filter(Job_author__pk=info.user.pk)
		# # applied=Application.objects.filter(author_id=info.pk, job_id=jobs.pk).count()
		# context = {
		# # 'category': category,
		# 'hjobs': hjobs,
		# 'Fjobs':Fjobs,
		# 'jobs': jobs,
		# 'form':form,
		# # 'applied':applied,
		# }
		# return render(request, template, context)
	else:
		template= 'home/index.html'
		# category = get_object_or_404(categories, pk=pk)
		hjobs= Hot_Jobs.objects.all()
		Fjobs= Featured_Jobs.objects.all()
		job = Job.objects.filter(is_active=True).order_by('-created_date')
		
		context = {
		# 'category': category,
		'hjobs': hjobs,
		'Fjobs':Fjobs,
		'job': job,
		
		}
		return render(request, template, context)

def Modls(request):
	template= 'home/models.html'
	modls= Pmodel.objects.all()
	context={
	'modls':modls,
	}
	return render(request, template, context)
