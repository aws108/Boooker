from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField

# Create your models here.

class Genero(models.Model):
	"""docstring for Missatges"""
	nombre=models.CharField(max_length=20,default='')
	"""incidencia=models.CharField(max_length=120)"""
	"""usuaris=models.ManyToManyField(Usuaris)"""
	def __str__(self):
		return self.nombre


class Libros(models.Model):
	"""docstring for Hashtags"""
	"""identificador=models.IntegerField(default=0)"""
	"""departament=models.ForeignKey(Departaments)"""
	nombre=models.CharField(max_length=50, default='')
	genero=models.ManyToManyField(Genero)
	portada=models.ImageField(upload_to='booker/images')
	contenido=models.FileField(upload_to='booker/libros',default='')
	sinopsis=models.TextField(max_length=600,default='')
	
	
	def __str__(self):
		return self.nombre

class Capitulos(models.Model):

	nombre=models.CharField(max_length=50, default='')
	libro=models.ForeignKey(Libros,default='')
	content = RichTextField(verbose_name='BookContent',null=True,blank=True)

	def __str__(self):
		return self.nombre

		