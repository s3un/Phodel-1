from django.urls import include, path
from django.conf.urls import url, include
from django.contrib.auth.views import login, password_reset
from django.contrib.auth import views as auth_views
from .views import ModelSignUpView, CompanySignUpView, SignUpView;
urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', SignUpView.as_view(), name='signup'),
    path('accounts/signup/model/', ModelSignUpView.as_view(), name='model_signup'),
    path('accounts/signup/company/', CompanySignUpView.as_view(), name='company_signup'),
    url(r'^login/$', login, {'template_name':'account/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
]