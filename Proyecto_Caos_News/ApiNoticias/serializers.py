from rest_framework import serializers 
from Web_CaosNew.models import Noticia

class NoticiaSerializers (serializers.ModelSerializer):
    class Meta:
        model = Noticia
        fields = ["titulo","subtitulo","historia","ubicacion","imagen","publicar","comentario","nombre","usuario"]