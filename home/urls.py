from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.contrib.auth.views import login
from django.conf import settings
from django.conf.urls.static import static 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
app_name = 'Home'
urlpatterns = [
	url(r'^$', views.Home.as_view(), name='index'),
    url(r'account/', include('account.urls'), name='account'),
    url(r'Job/', include('Jobs.urls'), name='Job'),
    # url(r'Product/', include('Product.urls'), name='Product'),
]
urlpatterns+=staticfiles_urlpatterns()
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 