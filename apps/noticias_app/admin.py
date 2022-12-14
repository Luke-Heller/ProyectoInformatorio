from django.contrib import admin
from .models import Categoria, Noticia, Comentario

#Convencion para poder hacer modificaciones en el admin de django a sus modelos
class CategoriaAdmin(admin.ModelAdmin):
    search_fields = ["nombre",]
    #Esto me hace habilitar como un filtro o barra de busqueda en el admin

    list_display = ("nombre","estado",)
    #Atributos (VERBOSE NAME COLOCADO EN MODELO) que queremos mostrar en el sitio de admin
    #Lista de atributos
class NoticiaAdmin(admin.ModelAdmin):
    # en el search lo que nos mostrara es en la vista del admin, esas columnas
    search_fields = ["titulo","categoria__nombre", "creado"]; #con los __ accedemos a un atributo en particular a para nuestro buscador

    #El list display es de que atributos(BD) saca esos datos para las colummnas
    list_display = ("titulo","autor","publicado","estado","categoria_noticia", "img");
    list_per_page = 10;
    # def comentarios_noticia(self,obj):
    #     return [c for c in obj.comentarios.all()];
    def categoria_noticia(self,obj):
        return [c for c in obj.categoria.all()]

# Register your models here.
admin.site.register(Noticia,NoticiaAdmin);
admin.site.register(Categoria,CategoriaAdmin);
admin.site.register(Comentario);