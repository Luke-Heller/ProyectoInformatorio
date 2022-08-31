from django.shortcuts import render, get_object_or_404  # Esto es lo que vamos a usar para poder ver el render
from django.http import HttpResponse
from django.views import View
from django.views.generic import DetailView, ListView, TemplateView
# from apps.noticias_app.models import *;
# Create your views here.
from apps.noticias_app.models import Noticia, Categoria


# def index(request): #Request lo recibe siempre
#     texto = {'mensaje_texto':"Esta es mi primera página",};
#     return render(request, 'indexCaducado.html',);

class Inicio (TemplateView):
    template_name = "indexOK.html";
    # contextvars
    def get_context_data(self, **kwargs):
        context = super(Inicio,self).get_context_data(**kwargs);
        context = {
            "texto_ayuda": "Ayudamos a mas de 100 niños",
            "merendero": "Merendero",
            "comunidad": "Mas de 5 años al servicio de la comunidad"
        }
        return context;



class ListadoNoticia(ListView):
    model = Noticia;
    template_name = "noticias/noticias.html";
    queryset = Noticia.objects.all();
    context_object_name = "noticias";
    paginate_by = 10;

class DetalleNoticia(DetailView):
    model = Noticia;
    template_name = "noticias/noticia-detalle.html";
    context_object_name = "noticia";

    # def get_context_data(self, **kwargs):
    #     context = super(DetalleNoticia, self).get_context_data(**kwargs);
    #     categorias = Categoria.objects.all();
    #
    #     context["categoriasxd"] = categorias;
    #
    #     return context;
