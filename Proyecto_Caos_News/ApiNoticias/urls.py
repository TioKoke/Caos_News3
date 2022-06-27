from django.urls import re_path as url
from rest_framework import urlpatterns
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

urlpatterns = [
    url(r'^api/noticias/$',NoticiasViewSet.as_view()),
    url(r'^api/buscar_autor/(?P<usuario>.+)/$',AutorBuscarViewSet.as_view()),
]   
urlpatterns= format_suffix_patterns(urlpatterns)