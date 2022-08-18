# Generated by Django 4.0.6 on 2022-08-17 22:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre de la Categoria')),
                ('estado', models.BooleanField(default=True, verbose_name='Categoria Activada / Categoria Desactivada')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('titulo', models.CharField(max_length=100, verbose_name='Titulo')),
                ('contenido', models.TextField()),
                ('img', models.ImageField(blank=True, help_text='Seleccione una imagen para mostrar', null=True, upload_to='media/images/noticias')),
                ('creado', models.DateTimeField(default=django.utils.timezone.now)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('publicado', models.DateTimeField(blank=True, null=True, verbose_name='Fecha de Publicacion')),
                ('estado', models.BooleanField(default=True, verbose_name='Noticia Activa / No activa')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('categoria', models.ManyToManyField(related_name='noticias', to='noticias_app.categoria', verbose_name='Categoria')),
            ],
            options={
                'verbose_name': 'Noticia',
                'verbose_name_plural': 'Noticias',
            },
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('cuerpo_comentario', models.TextField()),
                ('creado', models.DateTimeField(default=django.utils.timezone.now)),
                ('aprobado', models.BooleanField(default=False, verbose_name='Comentario Aprobado / No aprobado')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('noticia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='noticias_app.noticia')),
            ],
            options={
                'verbose_name': 'Comentario',
                'verbose_name_plural': 'Comentarios',
            },
        ),
    ]