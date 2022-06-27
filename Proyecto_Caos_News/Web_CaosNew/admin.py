#importar modelos
from django.contrib import admin
from .models import Categoria, Socio, Noticia, Galeria

# Register your models here.

admin.site.register(Categoria)
admin.site.register(Socio)
admin.site.register(Noticia)
admin.site.register(Galeria)
