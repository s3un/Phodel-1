from django.conf.urls import url, include
from . import views
urlpatterns = [
	url(r'^$', views.news, name='news'),
	url(r'^details/(?P<id>\w{0,10})/$', views.details, name='Ndetails'),
	]