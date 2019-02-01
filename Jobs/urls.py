from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.contrib.auth.views import login
from django.conf import settings
from django.conf.urls.static import static 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import JobCreateView,CompanyView, JobView, make_active, make_deactive,JobActiveStateView
urlpatterns = [
	# url(r'^$', views.Home.as_view(), name='index'),
    url(r'^create/$', JobCreateView.as_view(), name='job_create' ),
    url(r'^company/$', CompanyView.as_view(), name='company' ),
    url(r'^home/$', JobView, name='jobs' ),
    url(r'^Job/active/$', JobActiveStateView, name='preactivate' ),
    url(r'^active/(?P<pk>\d+)/$', make_active, name='active_jobs'),
    url(r'^deactive/(?P<dpk>\d+)/$', make_deactive, name='deactive_jobs'),
    # url(r'Product/', include('Product.urls'), name='Product'),
]
urlpatterns+=staticfiles_urlpatterns()
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 