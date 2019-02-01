from django.shortcuts import render, redirect,get_object_or_404
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from .models import Job, Hot_Jobs, Featured_Jobs
from .forms import JobModelForm
# Create your views here.

class JobCreateView(CreateView):
	template_name= 'Jobs/create.html'
	form_class = JobModelForm
	queryset = Job.objects.all()

class CompanyView(CreateView):
	template_name= 'Jobs/company_home.html'
	form_class = JobModelForm
	queryset = Job.objects.all()
	def get_success_url(self):
		return '/Job/company'

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
	