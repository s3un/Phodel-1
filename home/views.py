from django.shortcuts import render
from django.views import generic
from .models import Phodel
# Create your views here.
class Home(generic.TemplateView):
	template_name= 'home/index.html'
	context_object_name = 'name'
	queryset = Phodel.objects.all()
