from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from django.contrib.contenttypes.fields import GenericRelation
from star_ratings.models import Rating
from django.contrib.auth.models import User

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
	autores=models.ManyToManyField(User)
	nombre=models.CharField(max_length=50, default='')
	genero=models.ManyToManyField(Genero)
	portada=models.ImageField(upload_to='booker/images')
	contenido=models.FileField(upload_to='booker/libros',blank=True, null=True)
	sinopsis=models.TextField(max_length=600,default='')
	ratings = GenericRelation(Rating, related_query_name='foos')
	
	
	def __str__(self):
		return self.nombre

class Capitulos(models.Model):
	nombre=models.CharField(max_length=50, default='')
	libro=models.ForeignKey(Libros,default='')
	content = RichTextField(verbose_name='BookContent',null=True,blank=True)

	def __str__(self):
		return self.nombre

		