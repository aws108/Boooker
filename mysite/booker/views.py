from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.http import HttpResponse

from booker.models import *
# Create your views here.
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    # Redirect to a success page.

class LibrosCreateView(CreateView):
	model = Libros
	# indiquem la plantilla personalitzada i els camps que han d'apareixer al formulari
	# veureu que la plantilla es molt senzilla ja que fa tot el formulari amb {{form.as_p}}
	template_name = "libros.html"
	fields = ['nombre','genero','portada','contenido','sinopsis']

class Libros2CreateView(CreateView):
	model = Capitulos
	# indiquem la plantilla personalitzada i els camps que han d'apareixer al formulari
	# veureu que la plantilla es molt senzilla ja que fa tot el formulari amb {{form.as_p}}
	template_name = "editor.html"
	fields = ['nombre','libro','content']


def crea_capitol_view(request):
	pass


class LibrosListView(ListView):
	model = Libros
	template_name = "libroshecho.html"
	# si no posem template_name agafara per defecte karaoke/item_list.html
	def get_queryset(self):
		# nomes posem els items que estiguin per cantar
		return Libros.objects.all()
		#.filter(fet=False)

class LibrosAccionListView(ListView):
	model = Libros
	template_name = "libroshechoaccion.html"

	def get_queryset(self):
		# nomes posem els items que estiguin per cantar
		return Libros.objects.all()
		#.filter(fet=False)

class LibrosAventuraListView(ListView):
	model = Libros
	template_name = "libroshechoaventura.html"
	
	def get_queryset(self):
		# nomes posem els items que estiguin per cantar
		return Libros.objects.all()
		#.filter(fet=False)

class LibrosCienciaFiccionListView(ListView):
	model = Libros
	template_name = "libroshechocienciaficcion.html"
	
	def get_queryset(self):
		# nomes posem els items que estiguin per cantar
		return Libros.objects.all()
		#.filter(fet=False)

class LibrosHumorListView(ListView):
	model = Libros
	template_name = "libroshechohumor.html"
	
	def get_queryset(self):
		# nomes posem els items que estiguin per cantar
		return Libros.objects.all()
		#.filter(fet=False)

class LibrosMisterioListView(ListView):
	model = Libros
	template_name = "libroshechomisterio.html"
	
	def get_queryset(self):
		# nomes posem els items que estiguin per cantar
		return Libros.objects.all()
		#.filter(fet=False)

class LibrosRomanceListView(ListView):
	model = Libros
	template_name = "libroshechoromance.html"
	
	def get_queryset(self):
		# nomes posem els items que estiguin per cantar
		return Libros.objects.all()
		#.filter(fet=False)

class LibrosPoesiaListView(ListView):
	model = Libros
	template_name = "libroshechopoesia.html"
	
	def get_queryset(self):
		# nomes posem els items que estiguin per cantar
		return Libros.objects.all()
		#.filter(fet=False)

class LibrosTerrorListView(ListView):
	model = Libros
	template_name = "libroshechoterror.html"
	
	def get_queryset(self):
		# nomes posem els items que estiguin per cantar
		return Libros.objects.all()
		#.filter(fet=False)

class LibrosDramaListView(ListView):
	model = Libros
	template_name = "libroshechodrama.html"
	
	def get_queryset(self):
		# nomes posem els items que estiguin per cantar
		return Libros.objects.all()
		#.filter(fet=False)

class LibrosOtrosListView(ListView):
	model = Libros
	template_name = "libroshechootros.html"
	
	def get_queryset(self):
		# nomes posem els items que estiguin per cantar
		return Libros.objects.all()
		#.filter(fet=False)