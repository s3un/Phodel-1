from django.shortcuts import render, get_object_or_404,redirect
from django.views import generic
from .models import Phodel
import datetime
from Jobs.models import Job, Hot_Jobs, Featured_Jobs, Application, Offer
from django.contrib.auth.decorators import login_required
from Jobs.forms import JobModelForm
from account.models import Pmodel, Pcompany,CustomUser,images,interest
from django.db.models import Q
from news.models import News
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
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
def profile(request):
	if request.user.is_model==True:
		template= 'home/profile.html'
		profi = CustomUser.objects.get(pk=request.user.pk)
		info = Pmodel.objects.get(user__pk=profi.pk)
		imge = images.objects.filter(User__pk=info.pk)
		inter=interest.objects.filter(Users__pk=info.pk)
		# siz=int(info.model_image.size / 1024)
		context = {
		'profi':profi,
		'info':info,
		'imge':imge,
		'inter':inter,
		# 'siz':siz,
		}
		return render(request, template, context)
	if request.user.is_company==True:
		template= 'home/Company_profile.html'
		profi = CustomUser.objects.get(pk=request.user.pk)
		info = Pcompany.objects.get(user__pk=profi.pk)
		context = {
		'profi':profi,
		'info':info,
		}
		return render(request, template, context)
		
def LoginViews(request):
	if request.user.is_model==True:
		template= 'Jobs/jobs.html'
		profil = CustomUser.objects.get(pk=request.user.pk)
		info = Pmodel.objects.get(user__pk=profil.pk)
		appl= Application.objects.filter(applicant_id=info.pk)[:2]
		applcount=Application.objects.filter(applicant_id=info.pk)[:2].count()
		hjobs= Hot_Jobs.objects.all()
		Fjobs= Featured_Jobs.objects.all()
		news = News.objects.all()
		jobs = Job.objects.filter(is_active=True).order_by('-created_date')
		paginator = Paginator(jobs, 5)
		page = request.GET.get('page')
		job = paginator.get_page(page) 
		day=datetime.datetime.now()
		offer=Offer.objects.filter(applicant_id=info.pk)
		cont=Offer.objects.filter(applicant_id=info.pk).count()
		context = {
		'hjobs': hjobs,
		'Fjobs':Fjobs,
		'job': job,
		'appl':appl,
		'day':day,
		'news':news,
		'offer':offer,	
		'cont':cont,
		'applcount':applcount,
		}
		return render(request, template, context)
	elif request.user.is_company==True:
		return redirect('Home:company')
	else:
		template= 'home/index.html'
		hjobs= Hot_Jobs.objects.all()
		Fjobs= Featured_Jobs.objects.all()
		job = Job.objects.filter(is_active=True).order_by('-created_date')
		context = {
		'hjobs': hjobs,
		'Fjobs':Fjobs,
		'job': job,
		
		}
		return render(request, template, context)
def pages(request):
	template= 'Jobs/job_pages.html'
	jobs = Job.objects.filter(is_active=True).order_by('-created_date')
	paginator = Paginator(jobs, 1)
	page = request.GET.get('page')
	job = paginator.get_page(page)

	context={
	'job':job,
	}
	return render(request,template, context)

def Modls(request):
	template= 'home/models.html'
	modls= Pmodel.objects.all()
	context={
	'modls':modls,
	}
	return render(request, template, context)
