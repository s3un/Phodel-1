from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.contrib.auth.views import login
from django.conf import settings
from django.conf.urls.static import static 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
app_name = 'Home'
urlpatterns = [
	url(r'^$', views.Home, name='index'),
	url(r'^base/',views.base, name='bases'),
	url(r'^home/$', views.LoginViews, name='homeView'),
	url(r'^models/$', views.Modls, name='modl'),
	url(r'^Profile/$', views.profile, name='profile'),
    url(r'account/', include('account.urls'), name='account'),
    url(r'Job/', include('Jobs.urls'), name='Job'),
    url(r'News/', include('news.urls'), name='News'),
    # url(r'Product/', include('Product.urls'), name='Product'),
]
urlpatterns+=staticfiles_urlpatterns()
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 