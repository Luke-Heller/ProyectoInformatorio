from django.urls import include,path
from django.conf.urls.static import static
from django.conf import settings
from apps.noticias_app import views
app_name = "apps.noticias_app";

urlpatterns = [
    path('detalle/<uuid:pk>/', views.DetalleNoticia.as_view(), name='DetalleNoticia'),
] +static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT,show_indexes=True) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT,show_indexes=True)
