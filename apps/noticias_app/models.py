import datetime

import uuid;
from django.db import models
from django.utils import timezone
# Create your models here.

class Categoria(models.Model): #Tabla categoria
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False, unique=True, null=False, blank=False);
    nombre = models.CharField("Nombre de la Categoria",max_length=100);
    estado = models.BooleanField("Categoria Activada / Categoria Desactivada", default=True)

    # Verbose Name es la manera de como se va a identificar cada vez que se mencione a este modelo
    # de manera individual y plural en el sitio de admin de django
    class Meta():
        verbose_name = "Categoria";
        verbose_name_plural = "Categorias";

    def __str__(self):
        return self.nombre;

class Noticia(models.Model): #Tabla noticia
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True,  null=False, blank=False);
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE);
    titulo = models.CharField("Titulo",max_length=100);
    contenido = models.TextField();
    img = models.ImageField(null=True, blank=True, upload_to="images/noticias", help_text="Seleccione una imagen para mostrar");
    creado = models.DateTimeField(default=timezone.now);
    modificado = models.DateTimeField(auto_now=True);
    publicado = models.DateTimeField("Fecha de Publicacion",blank=True,null=True);

   # publicado = models.DateField("Fecha de Publicacion", auto_now= False, auto_now_add= True);
    categoria = models.ManyToManyField("Categoria", related_name="noticias", verbose_name="Categoria"); #RELACION UNA O MUCHAS
    estado = models.BooleanField("Noticia Activa / No activa", default=True)

    def __str__(self):
        return self.titulo;

    class Meta:
        verbose_name = "Noticia";
        verbose_name_plural = "Noticias"

    def publicarNoticia(self):
        self.publicado = datetime.date.today();
        self.save();

    def comentariosAprobados(self):
        return self.comentarios.filter(aprobado=True);

class Comentario(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, null=False, blank=False);
    noticia = models.ForeignKey("Noticia", related_name="comentarios", on_delete=models.CASCADE);
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE);
    cuerpo_comentario = models.TextField();
    creado = models.DateTimeField(default=timezone.now);
    aprobado = models.BooleanField("Comentario Aprobado / No aprobado",default=False);

    class Meta():
        verbose_name = "Comentario";
        verbose_name_plural = "Comentarios";

    def __str__(self):
        return f"Comentario {self.cuerpo_comentario}";

    def aprobarComentario(self):
        self.aprobado = True;
        self.save()