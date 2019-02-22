from django.urls import include, path
from django.conf.urls import url, include
from django.contrib.auth.views import login, password_reset
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.SignUpView.as_view(), name='signup'),
    path('accounts/signup/model/', views.ModelSignUpView.as_view(), name='model_signup'),
    path('accounts/signup/company/', views.CompanySignUpView.as_view(), name='company_signup'),
    url(r'^login/$', login, {'template_name':'account/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^Update-Career/(?P<pk>\d+)/$', views.Career.as_view(), name='career'), 
    url(r'^Update-Statistics/(?P<pk>\d+)/$', views.Statistics.as_view(), name='statistics'), 
    url(r'^Upload-Image/$', views.add_image.as_view(), name='upload_image'),
    url(r'^Add-Interest/$', views.add_interest.as_view(), name='interest_add'),
    url(r'^Remove/(?P<pk>\d+)/$', views.Remove_image, name='remove_image'),
    url(r'^Remove-interest/(?P<pk>\d+)/$', views.Remove_interest, name='remove_interest'), 
    url(r'^Update-details/(?P<pk>\d+)/$', views.ImageUpdate.as_view(), name='detail_update'),    
]