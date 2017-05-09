"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
"""from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include

urlpatterns = [
	url(r'^booker/', include('booker.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^login/', include('social.apps.django_app.urls', namespace='social')),
]"""

import django


from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from booker import views
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import *


urlpatterns = [ 
	url(r'^admin/', include(admin.site.urls)),
	# Python Social Auth URLs
	url('', include('social.apps.django_app.urls', namespace='social')),
	url(r'^accounts/', include('registration.urls')),
	# Home URL
	url(r'^$', TemplateView.as_view(template_name="home.html"), name="home"),

    #FORMULARIO
	url(r'^libros/', views.LibrosCreateView.as_view(success_url='/hecho'), name="compres" ),

    #CKEDITOR
    url(r'^editor/', views.Libros2CreateView.as_view(success_url='/editor'), name="editor" ),
    #url(r'^editor2/'

    #TODOS LOS LIBROS
	url(r'^hecho/', views.LibrosListView.as_view(), name="hecho"),

    #GENEROS
    url(r'^accion/', views.LibrosAccionListView.as_view(), name="accion"),
    url(r'^aventura/', views.LibrosAventuraListView.as_view(), name="aventura"),
    url(r'^cienciaficcion/', views.LibrosCienciaFiccionListView.as_view(), name="cienciaficcion"),
    url(r'^humor/', views.LibrosHumorListView.as_view(), name="humor"),
    url(r'^misterio/', views.LibrosMisterioListView.as_view(), name="misterio"),
    url(r'^romance/', views.LibrosRomanceListView.as_view(), name="romance"),
    url(r'^poesia/', views.LibrosPoesiaListView.as_view(), name="poesia"),
    url(r'^terror/', views.LibrosTerrorListView.as_view(), name="terror"),
    url(r'^drama/', views.LibrosDramaListView.as_view(), name="drama"),
    url(r'^otros/', views.LibrosOtrosListView.as_view(), name="otros"),

	# Logout URL
	url( r'^users/logout/$', auth_views.LogoutView.as_view() , {'next_page': '/'}, name="user-logout" ),


	#url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
    #   'document_root': settings.STATIC_ROOT
    #}),
    url(r'^media/(?P<path>.*)$', django.views.static.serve, {
        'document_root': settings.MEDIA_ROOT
    }),
    url(r'^djrichtextfield/', include('djrichtextfield.urls')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
]

#urlpatterns += staticfiles_urlpatterns()
#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
