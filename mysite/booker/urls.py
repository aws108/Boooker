from django.conf.urls import url

from . import views

from django.conf.urls import include, url 
from django.contrib import admin 
from django.views.generic import TemplateView


urlpatterns = [ 
	#url(r'^$', TemplateView.as_view(template_name="home.html"), name="home"), 
	#url( r'^users/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name="user-logout" ), 
]
