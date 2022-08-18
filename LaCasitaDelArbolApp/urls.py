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
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.urls import re_path;
from LaCasitaDelArbolApp import settings
from apps.noticias_app import views
from django.conf.urls.static import static;
# va a contener la lista de todos los enlaces que van a contener mi aplicacion

# django viene, busca el contexto en url, dice es una vista o un conjunto de urls, despues se va a views y ve cual es el html que va a responder.
#  NO SE PUEDEN CREAR VISTAAS SI AL MENOS NO HAY UNA APLICACION, EN ESTE CASO NOTICIAS

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', views.index, name='index'),#ESTO SE VINCULA CON LAS VISTAS CREADAS EN VIEWS (LLAMAMOS A LA FUNCION QUE ESTA EN VIEWS)
    path('nosotros/',views.nosotros, name='nosotros'),
    path('noticias/',views.NoticiaListView.as_view(), name='noticias'),
]#+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT, show_indexes = True)+static();
