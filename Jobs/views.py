from django.shortcuts import render, redirect,get_object_or_404, HttpResponse
from django.views.generic.edit import CreateView, View
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from .models import Job, Hot_Jobs, Featured_Jobs, Application,Lga,States
from account.models import Pmodel, Pcompany,CustomUser,images,interest
from .forms import JobModelForm
from django.contrib import messages
# Create your views here.

class JobCreateView(CreateView):
	template_name= 'Jobs/create.html'
	form_class = JobModelForm
	queryset = Job.objects.all()

def loadLga(request):
	state_id = request.GET.get('state')
	lga = Lga.objects.filter(state_id=state_id).order_by('lga')
	return render(request, 'Jobs/lga.html', {'lga':lga})

class CompanyView(View):
	template_name= 'Jobs/company_home.html'
	form_class = JobModelForm
	def get(self, request):
		form=self.form_class(None)
		hjobs= Hot_Jobs.objects.all()
		Fjobs= Featured_Jobs.objects.all()
		profil = CustomUser.objects.get(pk=request.user.pk)
		info = Pcompany.objects.get(user__pk=profil.pk)
		jobs = Job.objects.filter(Job_author__pk=info.user.pk)
		# applied=Application.objects.filter(author_id=info.pk, job_id=jobs.pk).count()
		context = {
		# 'category': category,
		'hjobs': hjobs,
		'Fjobs':Fjobs,
		'jobs': jobs,
		'form':form,
		# 'applied':applied,
		}
		return render(request, self.template_name, context)
	def post(self,request, **kwargs):
		form=self.form_class(request.POST)
		if form.is_valid():
			create=form.save(commit=False)
			c= form.cleaned_data
			Job_title=c['Job_title'],
			Job_author=c['Job_author'],
			state=c['state'],
			lga=c['lga'],
			town =c['town'],
			gender=c['gender'],
			height=c['height'],
			Job_Description=c['Job_Description'],
			personal_note=c['personal_note'],
			street_address=c['street_address'],
			create.save()
			return redirect('Home:company')



# class JobView(TemplateView):
# 	template_name= 'Jobs/jobs.html'
# 	context_object_name= 'name'
# 	queryset = Job.objects.all().order_by('-created_date')

# 	def get_context_data(self, **kwargs):
# 	    context = super(JobView, self).get_context_data(**kwargs)
# 	    context['hjobs']= Hot_Jobs.objects.all()
# 	    context['Fjobs']= Featured_Jobs.objects.all()
# 	    context['job']= self.queryset
# 	    return context
def JobView(request):
	template= 'Jobs/jobs.html'

	# category = get_object_or_404(categories, pk=pk)
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
def JobActiveStateView(request):
	template= 'Jobs/Preactivate.html'
	# category = get_object_or_404(categories, pk=pk)
	hjobs= Hot_Jobs.objects.all()
	Fjobs= Featured_Jobs.objects.all()
	job = Job.objects.all().order_by('-created_date')
	
	context = {
	# 'category': category,
	'hjobs': hjobs,
	'Fjobs':Fjobs,
	'job': job,
	
	}
	return render(request, template, context)
def make_active(request, pk):
	jobs = get_object_or_404(Job, pk=pk)
	jobs.is_active=True
	jobs.save()
	return redirect('Home:jobs')

def make_deactive(request, dpk):
	jobs=get_object_or_404(Job, pk=dpk)
	jobs.is_active=False
	jobs.save()
	return redirect('Home:jobs')

def job_detail(request, pk):
	template= 'Jobs/job_detail.html'
	profil = CustomUser.objects.get(pk=request.user.pk)
	info = Pmodel.objects.get(user__pk=profil.pk)
	job = Job.objects.get(pk=pk)
	applied=Application.objects.filter(job_id=job.pk, applicant_id=info.pk)
	if applied.exists():
		go=True
		context= {
		'job': job,
		'applied':applied,
		'go':go
		}
		return render(request, template, context)
	else:
		go=False
		context= {
		'job': job,
		'applied':applied,
		'go':go
		}
		return render(request, template, context)


def Apply(request,pk):
	profil = CustomUser.objects.get(pk=request.user.pk)
	info = Pmodel.objects.get(user__pk=profil.pk)
	job = Job.objects.get(pk=pk)
	applying= Application.objects.create(
		Job_title=job.Job_title,
		job_id=job.pk, 
		Job_author=job.Job_author.username,
		applicant=info.first_name+' '+info.last_name,
		applicant_id=info.pk,
		author_id=job.Job_author.pk,
		)
	return redirect('Home:homeView')



def application(request, pk):
	template='Jobs/applications.html'
	profil = CustomUser.objects.get(pk=request.user.pk)
	info = Pcompany.objects.get(user__pk=profil.pk)
	jobs = Job.objects.get(pk=pk)
	appl=Application.objects.filter(author_id=profil.pk, job_id=jobs.pk)
	# applicants=Pmodel.objects.filter()
	context={
	'info':info,
	'appl':appl,
	'jobs':jobs,
	'profil':profil
	}
	return render(request, template, context)

@login_required
def Check(request, pk,jpk):
	template="Jobs/check_profile.html"
	profil = CustomUser.objects.get(pk=request.user.pk)
	info= Pmodel.objects.get(pk=pk)
	image= images.objects.filter(User__pk=info.pk)
	appl=Application.objects.get(author_id=profil.pk, job_id=jpk, applicant_id=info.pk)
	job=jpk	
	context={
	'info':info,
	'image':image,
	'appl':appl,
	'job':job,
	}
	return render(request,template,context)

def set_active(request, pk, jpk):
	template='Jobs/applications.html'
	profil = CustomUser.objects.get(pk=request.user.pk)
	info = Pcompany.objects.get(user__pk=profil.pk)
	jobs = Job.objects.get(pk=jpk)
	appl=Application.objects.filter(author_id=profil.pk, job_id=jobs.pk)
	# applicants=Pmodel.objects.filter()
	application = get_object_or_404(Application, pk=pk)
	application.status=1
	application.save()
	context={
	'info':info,
	'appl':appl,
	'jobs':jobs,
	'profil':profil
	}
	return render(request, template, context)

def set_deactive(request, pk, jpk):
	template='Jobs/applications.html'
	profil = CustomUser.objects.get(pk=request.user.pk)
	info = Pcompany.objects.get(user__pk=profil.pk)
	jobs = Job.objects.get(pk=jpk)
	appl=Application.objects.filter(author_id=profil.pk, job_id=jobs.pk)
	# applicants=Pmodel.objects.filter()
	application = get_object_or_404(Application, pk=pk)
	application.status=2
	application.save()
	context={
	'info':info,
	'appl':appl,
	'jobs':jobs,
	'profil':profil
	}
	return render(request, template, context)

