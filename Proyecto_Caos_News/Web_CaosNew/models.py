
from enum import auto
from pyexpat import model
from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(primary_key=True,max_length=20)
    imagen = models.ImageField(upload_to='fotos',null=True,default='Falta_imagen.jpg')
    
    def __str__(self):
        return self.nombre

class Socio(models.Model):
    nombre = models.CharField(primary_key=True,max_length=45)
    password = models.CharField(max_length=60)
    correo = models.CharField(max_length=60)

    def __str__(self):
        return self.nombre

class Noticia(models.Model):
    titulo = models.CharField(primary_key=True,max_length=300,default='--')
    subtitulo = models.CharField(max_length=300,default='--')
    historia = models.CharField(max_length=10000,default='--')
    ubicacion = models.CharField(max_length=80,default='--')
    imagen = models.ImageField(upload_to='fotos',null=True,default='Falta_imagen.jpg')
    publicar = models.BooleanField(default=False)
    comentario = models.TextField(default='--')
    nombre = models.ForeignKey(Categoria,on_delete=models.CASCADE,default='--')
    usuario = models.CharField(max_length=60,default='--')

    def __str__(self):
        return self.titulo

class Galeria(models.Model):
    auto_inc = models.AutoField(primary_key=True)
    imagen = models.ImageField(upload_to='galeria')
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE)
    def __str__(self):
        return 'Numero:'+str(self.auto_inc)

class Contacto(models.Model):
    contador = models.AutoField(primary_key=True)
    rut = models.CharField(max_length=300,default='--')
    nombre = models.CharField(max_length=300,default='--')
    correo = models.CharField(max_length=300,default='--')
    telefono = models.CharField(max_length=300,default='--')
    region = models.CharField(max_length=300,default='--')
    ciudad = models.CharField(max_length=300,default='--')
    termino = models.BooleanField(default=False)
    def __str__(self):
        return 'Numero:'+str(self.contador)