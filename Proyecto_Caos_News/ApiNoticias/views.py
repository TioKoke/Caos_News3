from django.shortcuts import render
from .serializers import NoticiaSerializers
from rest_framework import generics
from Web_CaosNew.models import Noticia
# Create your views here.

class NoticiasViewSet(generics.ListAPIView):
    queryset = Noticia.objects.all()
    serializer_class = NoticiaSerializers

class AutorBuscarViewSet(generics.ListAPIView):
    serializer_class = NoticiaSerializers
    def get_queryset(self):
        autor_noticia = self.kwargs["usuario"]
        return Noticia.objects.filter(usuario = autor_noticia)

