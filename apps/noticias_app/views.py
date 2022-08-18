from django.shortcuts import render #Esto es lo que vamos a usar para poder ver el render
from django.http import HttpResponse
from django.views.generic import DetailView, ListView
# from apps.noticias_app.models import *;
# Create your views here.
from apps.noticias_app.models import Noticia


def index(request): #Request lo recibe siempre
    texto = {'mensaje_texto':"Esta es mi primera pagina",};
    return render(request, 'index.html',);



def nosotros(request):
    return None;

class NoticiaListView(ListView):
    model = Noticia;
    template_name = "noticias/noticiaPruebaBS.html";
