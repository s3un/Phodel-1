from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.contrib.auth.views import login
from django.conf import settings
from django.conf.urls.static import static 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
urlpatterns = [
	# url(r'^$', views.Home.as_view(), name='index'),
    url(r'^create/$', views.JobCreateView.as_view(), name='job_create' ),
    url(r'^company/$', views.CompanyView.as_view(), name='company' ),
    url(r'^home/$', views.JobView, name='jobs' ),
    url(r'^Applications/(?P<pk>\d+)/$', views.Apply, name='apply' ),
    url(r'^lga/$', views.loadLga, name='load_lga'),
    url(r'^Job/Job_details/(?P<pk>\d+)/$', views.job_detail, name='jobdetails' ),
    url(r'^check/(?P<pk>\d+)/(?P<jpk>\d+)/$', views.Check, name='model_profile' ),
    url(r'^Job/active/$', views.JobActiveStateView, name='preactivate' ),
    url(r'^active/(?P<pk>\d+)/$', views.make_active, name='active_jobs'),
    url(r'^deactive/(?P<dpk>\d+)/$', views.make_deactive, name='deactive_jobs'),    
    url(r'^Application/(?P<pk>\d+)/$', views.application, name='applicate'),
    url(r'^Approve/(?P<pk>\d+)/(?P<jpk>\d+)/$', views.set_active, name='approve'),
    url(r'^Decline/(?P<pk>\d+)/(?P<jpk>\d+)/$', views.set_deactive, name='decline'),
    # url(r'Product/', include('Product.urls'), name='Product'),
]
urlpatterns+=staticfiles_urlpatterns()
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 