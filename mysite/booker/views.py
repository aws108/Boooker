from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView
from django.http import HttpResponse
from django import forms
from booker.models import *
# Create your views here.

from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return render( request, 'visualizadorlibros.html')


class EditorForm(forms.ModelForm):
    class Meta:
       model = Capitulos
       fields = ['nombre','libro','content']

    def __init__(self, *args, **kwargs):
       user = kwargs.pop('user')
       super(EditorForm, self).__init__(*args, **kwargs)
       self.fields['libro'].queryset = Libros.objects.filter(autores=user)

class Faq(CreateView):
	model = Libros
	# indiquem la plantilla personalitzada i els camps que han d'apareixer al formulari
	# veureu que la plantilla es molt senzilla ja que fa tot el formulari amb {{form.as_p}}
	template_name = "faq.html"
	fields = ['nombre','autores','genero','portada','contenido','sinopsis']

class SubeCreaLibro(CreateView):
	model = Libros
	template_name = "subecrealibro.html"
	fields = ['nombre','autores','genero','portada','contenido','sinopsis']

class LibrosCreateView(CreateView):
	model = Libros
	# indiquem la plantilla personalitzada i els camps que han d'apareixer al formulari
	# veureu que la plantilla es molt senzilla ja que fa tot el formulari amb {{form.as_p}}
	template_name = "libros.html"
	fields = ['nombre','autores','genero','portada','contenido','sinopsis']

class LibrosDesdeCero(CreateView):
	model = Libros
	# indiquem la plantilla personalitzada i els camps que han d'apareixer al formulari
	# veureu que la plantilla es molt senzilla ja que fa tot el formulari amb {{form.as_p}}
	template_name = "librosdesdecero.html"
	fields = ['nombre','autores','genero','portada','sinopsis']

class Libros2CreateView(CreateView):
	# indiquem la plantilla personalitzada i els camps que han d'apareixer al formulari
	# veureu que la plantilla es molt senzilla ja que fa tot el formulari amb {{form.as_p}}
	template_name = "editor.html"
	form_class = EditorForm

	def get_form_kwargs(self):
		kwargs = super(Libros2CreateView, self).get_form_kwargs()
		kwargs['user'] = self.request.user
		return kwargs

class CapitulosDeleteView(DeleteView):
	model = Capitulos
	success_url = '/hecho'
	template_name = 'capitulos_confirm_delete.html'

	def get_queryset(self):
		folders = Capitulos.objects.filter(libro__autores=self.request.user)
		return folders

class LibrosDeleteView(DeleteView):
	model = Libros
	success_url = '/hecho'
	template_name = 'capitulos_confirm_delete.html'

	def get_queryset(self):
		folders = Libros.objects.filter(autores=self.request.user)
		return folders

class EditorCapitulos(UpdateView):
    model = Capitulos
    success_url = '/hecho'
    fields = ['nombre','content']
    template_name = 'editorcapitulos.html'

#VIEW PERSONALIZADA
#VIEW Para pasar capitulos
def visualizadorlibros(request,visualiza):
	identificador = visualiza
	
	capitulos = Capitulos.objects.filter(libro=identificador).order_by('id')

	#for capitulo in capitulos:
	

	
	return render( request, 'visualizadorlibros.html' , {"caps":capitulos} )



def visualizadorcapitulos(request,visualiza2):
	identificador2 = visualiza2

	capitulos = Capitulos.objects.filter(id=identificador2)

	borrable = False
	for cap in capitulos:
		if request.user in cap.libro.autores.all() :
			borrable = True

	return render( request, 'visualizadorcapitulos.html' , {"caps":capitulos,"borrable":borrable} )

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