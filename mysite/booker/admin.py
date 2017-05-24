from django.contrib import admin

# Register your models here.

from .models import Genero

admin.site.register(Genero)

from .models import Libros

admin.site.register(Libros)

from .models import Capitulos


class CapituloAdmin(admin.ModelAdmin):
	list_display = ['nombre','libro']

admin.site.register(Capitulos,CapituloAdmin)

