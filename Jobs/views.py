from django.shortcuts import render, redirect,get_object_or_404, HttpResponse
from django.views.generic.edit import CreateView, View
from django.views.generic import TemplateView
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from .models import Job, Hot_Jobs, Featured_Jobs, Application,Lga,States, Offer
from account.models import Pmodel, Pcompany,CustomUser,images,interest
from .forms import JobModelForm
from django.contrib import messages
from django.core.mail import EmailMessage, send_mail, EmailMultiAlternatives
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

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
			form.save_m2m()
			return HttpResponse('Job Successfully added and awaiting Approval')

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
	return HttpResponse('Activated')

def remove_job(request, pk):
	jobs = get_object_or_404(Job, pk=pk).delete()
	return HttpResponse('Job Removed')

def make_deactive(request, dpk):
	jobs=get_object_or_404(Job, pk=dpk)
	jobs.is_active=False
	jobs.save()
	return HttpResponse('Job Deactivated')

def job_detail(request, pk):
	template= 'Jobs/job_detail.html'
	profil = CustomUser.objects.get(pk=request.user.pk)
	info = Pmodel.objects.get(user__pk=profil.pk)
	job = Job.objects.get(pk=pk)
	applied=Application.objects.filter(job_id=job.pk, applicant_id=info.pk)
	if applied.exists():
		appl=Application.objects.get(job_id=job.pk, applicant_id=info.pk)
		go=True
		context= {
		'job': job,
		'applied':applied,
		'go':go,
		'appl':appl
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
		applicant=info.last_name+' '+info.first_name,
		applicant_id=info.pk,
		author_id=job.Job_author.pk,
		applicant_mail=info.email,
		)
	mail_subject = 'Job Application Recieved.'
	message = render_to_string('Jobs/job_received.html', {            
		'applicant': info.last_name+' '+info.first_name,
		'Job_author':job.Job_author.username,
		'Job_title':job.Job_title,
	})
	to_email = [
	info.email,
	]
	# msg_plain = render_to_string('templates/email.txt', {'some_params': some_params})
	msg_html = render_to_string('Jobs/job_received.html', {            
		'applicant': info.last_name+' '+info.first_name,
		'Job_author':job.Job_author.username,
		'Job_title':job.Job_title,
	})

	send_mail(mail_subject, message, 'Temidire@phodel.com.ng', to_email, fail_silently=False, html_message=msg_html, )
	context = {
	'job':job,
	}
	return render(request,'Jobs/job_sent.html',context)



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
	'profil':profil,

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
#status code 1 is shortlisted
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
	mail_subject = 'Job Application Status.'
	message = render_to_string('Jobs/status.txt', {            
		'applicant': application.applicant,
		'Job_author':application.Job_author,
		'Job_title':application.Job_title,
		'status':application.status

	})
	to_email = [
	application.applicant_mail,
	]
	msg_html = render_to_string('Jobs/status.html', {            
		'applicant': application.applicant,
		'Job_author':application.Job_author,
		'Job_title':application.Job_title,
		'status':application.status

	})

	send_mail(mail_subject, message, 'Temidire@phodel.com.ng', to_email, fail_silently=False, html_message=msg_html, )
	context={
	'info':info,
	'appl':appl,
	'jobs':jobs,
	'profil':profil
	}
	return render(request, template, context)
#status code 2 is declined
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
	mail_subject = 'Job Application Status.'
	message = render_to_string('Jobs/status.txt', {            
		'applicant': application.applicant,
		'Job_author':application.Job_author,
		'Job_title':application.Job_title,
		'status':application.status

	})
	to_email = [
	application.applicant_mail,
	]
	# msg_plain = render_to_string('templates/email.txt', {'some_params': some_params})
	msg_html = render_to_string('Jobs/status.html', {            
		'applicant': application.applicant,
		'Job_author':application.Job_author,
		'Job_title':application.Job_title,
		'status':application.status

	})

	send_mail(mail_subject, message, 'Temidire@phodel.com.ng', to_email, fail_silently=False, html_message=msg_html, )
	context={
	'info':info,
	'appl':appl,
	'jobs':jobs,
	'profil':profil
	}
	return render(request, template, context)

def offers(request, pk):
	if request.method == 'GET':
		template= 'Jobs/offer.html'
		profil = CustomUser.objects.get(pk=request.user.pk)
		modl = Pmodel.objects.get(pk=pk)
		info = Pcompany.objects.get(user__pk=profil.pk)
		jobs = Job.objects.filter(Job_author__pk=info.user.pk)

		context={
		'profil':profil,
		'info':info,
		'jobs':jobs,
		'modl':modl,
		}
		return render(request, template, context) 
	elif request.method == 'POST':
		profil = CustomUser.objects.get(pk=request.user.pk)
		modl = Pmodel.objects.get(pk=pk)
		info = Pcompany.objects.get(user__pk=profil.pk)
		jobs = Job.objects.filter(Job_author__pk=info.user.pk)
		jobo=Job.objects.get(pk=request.POST.get('Jobs'))
		offer = Offer.objects.create(
			job=jobo,
			applicant=modl.last_name+' '+modl.first_name,
			applicant_id=modl.pk,
			applicant_mail=modl.email,
			author_id=info.pk,
			)
		mail_subject = 'New Job Offer'
		message = render_to_string('Jobs/offer_mail.txt', {            
			'applicant': modl.last_name+' '+modl.first_name,
			'Job_author':jobo.Job_author.username,
			'Job_title':jobo.Job_title,
		})
		to_email = [
		modl.email,
		]
		msg_html = render_to_string('Jobs/offer_mail.html', {            
			'applicant': modl.last_name+' '+modl.first_name,
			'Job_author':jobo.Job_author.username,
			'Job_title':jobo.Job_title,

		})

		send_mail(mail_subject, message, 'Temidire@phodel.com.ng', to_email, fail_silently=False, html_message=msg_html, )
		return redirect('Home:modl')

def Job_offers(request, pk):
	template= 'Jobs/check_offers.html'
	profil = CustomUser.objects.get(pk=request.user.pk)
	info = Pmodel.objects.get(user__pk=profil.pk)
	jobs= Job.objects.get(pk=pk)
	offer = Offer.objects.get(job=jobs, applicant_id=info.pk)

	context={
	'profil':profil,
	'info':info,
	'jobs':jobs,
	'offer':offer
	}
	return render(request, template, context)

#offer acepted
def offers_accept(request, pk):
	offer = get_object_or_404(Offer,pk=pk)
	offer.status=1
	offer.save()
	applying= Application.objects.create(
	Job_title=offer.job.Job_title,
	job_id=offer.job.pk, 
	Job_author=offer.job.Job_author.username,
	applicant=offer.applicant,
	applicant_id=offer.applicant_id,
	author_id=offer.job.Job_author.pk,
	applicant_mail=offer.applicant_mail,
	status=1,
	)
	return redirect('Home:homeView')

# offer declined
def offers_decline(request, pk):
	offer = get_object_or_404(Offer,pk=pk).delete()
	return redirect('Home:homeView')