"""LaCasitaDelArbolApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls.py import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls.py'))
"""
from django.contrib import admin
from django.urls import re_path as url;
from django.urls import path, include
from django.conf import settings;
# from apps.noticias_app import views
from django.conf.urls.static import static;

from apps.noticias_app.views import Inicio, ListadoNoticia

# va a contener la lista de todos los enlaces que van a contener mi aplicacion

# django viene, busca el contexto en url, dice es una vista o un conjunto de urls.py, despues se va a views y ve cual es el html que va a responder.
#  NO SE PUEDEN CREAR VISTAAS SI AL MENOS NO HAY UNA APLICACION, EN ESTE CASO NOTICIAS

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', Inicio.as_view(), name='index'),#ESTO SE VINCULA CON LAS VISTAS CREADAS EN VIEWS (LLAMAMOS A LA FUNCION QUE ESTA EN VIEWS)
    path('noticias/', ListadoNoticia.as_view(), name='noticias'),
    # path("noticia-detalle/<int:id>", DetalleNoticia.as_view(), name='detalle_noticia'),
    url('noticia/', include('apps.noticias_app.urls', namespace="apps.noticias_app"),),
 ]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT,show_indexes=True) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT,show_indexes=True)+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT,show_indexes=True) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT,show_indexes=True);

