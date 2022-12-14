"""
Django settings for LaCasitaDelArbolApp project.

Generated by 'django-admin startproject' using Django 4.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os
import sys

# Build paths inside the project like this: BASE_DIR / 'subdir'.
#BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)));


"""
BASE_DIR: NOS PERMITE DEFINIR COMO ESTAN COMPUESTA TODAS LAS RUTAS QUE FORMAN PARTE 
DE MI PROYECTO
COMPLETA LA PRIMER PARTE DE TODA LA RUTA, ENTONCES LO QUE TENDRIAMOS QUE HACER ES
PONER LA BARRA / Y LLAMAR AL NOMBRE DEL ARCHIVO O AL NOMBRE DE LA CARPETA

ESTO NOS SIRVE PARA QUE CUANDO PASEMOS EL PROYECTO LA DETECTE AUTOMATICAMENTE AL PROYECTO CON 
EL LLAMADO "OS"  

LLAMA AL PATH DEFINIDO POR EL S.O. Y BUSCA CUAL ES ESA RUTA, O DONDE SE ENCUENTRA PARADO ACTUALMENTE EL PROYECTO
"""


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ''
"""
ESTA SECRET KEY ES UNICA PARA CADA PROYECTO, ES DECIR QUE UNO DEBE CREAR EL PROYECTO Y LAS OTRAS PERSONAS LO CLONEN.
POR QUE CADA VEZ QUE EJECUTEMOS EL COMANDO START PROYECT ESTA SECRET KEY ES DISTINTA PARA TODOS LOS CASOS.
CUANDO SUBAMOS EL PROYECTO A GITHUB DEBEREMOS SUBIRLA ASI: "" (VACIO) POR QUE SI LA SUBIMOS AL REPO, NOS MANDARA UN ALERTA
DE QUE ESTAMOS SUBIENDO INFO SENSIBLE, ENTONCES HAY QUE SUBIR SIN LA SECRET KEY OK?

"""


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
"""
ESTA VARIABLE DEBUG ES LA QUE PERMITE QUE SI SE PRODUCE UN ERROR, NOS MUESTRA LA LINEA Y LA POSICION EXACTA DE DONDE SE ENCUENTRA
EL ERROR. CUANDO SUBAMOS ESTO A PRODUCCION, EN EL SETTINGS DE NUESTRO ARCHIVO "production.py" VAMOS A TENER QUE REDEFINIR ESA VARIABLE
DEBUG Y PONERLA EN "FALSE", PARA QUE SEA EL ERROR QUE HAYA EN PRODUCCION, NO SE MUESTRE NADA.

SI LA DEJAMOS A BASE EN TRUE Y SUBIMOS A PRODUCCION, Y SE MUESTRA ALGUNO DE LOS ERRORES, PODRIA SALIR HASTA LA RUTA EXACTA DE DONDE SE 
ENCUENTRA NUESTRO ARCHIVO

//// DEBUG TIENE QUE ESTAR EN TRUE SIEMPRE QUE NOSOTROS TRABAJEMOS EN LOCAL O EN OTRO SERVIDOR QUE NO SEA PRODUCCION!!! ///
"""

ALLOWED_HOSTS = []
"""
Esta variable "ALLOWED_HOSTS" tambien se va a volver a redefinir en produccion, ya que aqui vamos a colocar cual es la URL DE MI SITIO
QUE ES LA QUE LE VA A DECIR A DJANGO DONDE O DE QUE SERVIDOR TIENE QUE RECIBIR PETICIONES Y PERMITIR QUE LA PAGINA SE CARGUE

Como yo estoy en local, no tengo ninguna url dominio, no tengo servidor, estoy en el servidor local
LO DEJO VACIO.

Como vemos que es un archivo tipo lista, puede ser que hasta podamos tener mas de un servidor
"""


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.noticias_app'
]
"""
INSTALLED_APPS CONTIENE TODAS LAS APPS QUE TRAE DJANGO POR DEFECTO.

# admin -> tiene todas las funciones relacionadas a la parte del panel de administracion
# auth: -> tiene todas las funciones relacionadas a la parte de autenticacion (login, logout, autenticacion de usuarios, etc)
# contenttypes -> tiene todo lo relacionado a la gestion del contenido, es decir si queremos crear tablas nuevas, apps nuevas
que tengan que generar datos, ej todas las noticias que se carguen al blog usaran estas funciones.
# sessions -> Todo lo relacionado a las sesiones, iniciar sesion, salir de sesion.
# messages -> Toda la parte de mensajes
# staticfiles -> Nos permite agregar archivos, subir archivos, eliminar archivos, etc.

Cuando creemos nuestra app de blog y de eventos aqui tendremos que agregar esas nuevas aplicaciones para poder trabajar con eso.
"""

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
"""
Esto contiene los distintos tipos de aplicaciones de componentes que manejan funciones en la parte de autenticacion, mensajes...
Tanto middleware como installed apps son funciones que ya traen django por defecto para que nosotros podamos hacer mas facil o mucho mas rapido
toda la parte de gestion de contenido, autenticacion, panel de control, control de password para que sea seguro, etc.

"""

ROOT_URLCONF = 'LaCasitaDelArbolApp.urls'
"""
Contiene cual es la direccion (PATH) donde esta mi archivo "urls.py". Si o si tiene que estar correcta porque cada vez que hagamos click en un enlace
django viene al archivo settings ejecutado en el manage y busca cual es mi archivo de urls para saber cual es la vista o el template que tiene que cargar.


"""

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(os.path.dirname(BASE_DIR),'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
"""
Aqui tenemos cual es la direccion a la carpeta de templates.
LA MODIFICACION DE LA LINEA DIRS SERIA: os.path.join(os.path.dirname(BASE_DIR,'templates'))

"""

WSGI_APPLICATION = 'LaCasitaDelArbolApp.wsgi.application'
"""
Aqui contiene la ruta de nuestro archivo wsgi donde despues vamos a definir para subir a produccion.

"""

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(os.path.dirname(BASE_DIR),'db.sqlite3'),
    }
}
"""
Aqui definimos cual es la base o el motor de BD que vamos a utilizar.
En este caso como lo unico que vamos a hacer o lo unico que vamos a usar base va a ser para montar nuestro proyecto
por primera vez, vamos a dejar sqlite3, ya que despues cuando tengamos que ejecutarlo en local o produccion vamos a ejecutar
el motor que corresponda.
LO QUE HICIMOS FUE DECIRLE DONDE TIENE QUE BUSCAR ESA LIBRERIA DE SQLITE3 

(EN CASO DE NECESITAR MODIFICAR LA RUTA DE NAME SERIA: os.path.join(os.path.dirname(BASE_DIR),'db.sqlite3') 
"""

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
"""
Aqui tenemos todas las librerias relacionadas a las partes de validaciones, las cantidades minimas de caracteres,
si tiene los caracteres que son comunes, que tengan al menos numero, al menos mayuscula, al menos signo

"""


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'es-ar'

TIME_ZONE = 'America/Argentina/Buenos_Aires'

USE_I18N = True

USE_TZ = True
"""
Aca definiremos de que idioma va a ser nuestra app, modificaremos el idioma y la zona horaria
"""

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(os.path.dirname(BASE_DIR),'static')), #path manual creado por la profe

MEDIA = '/media/' #VARIABLE CREADA PARA ENCOONTRAR LOS MEDIA
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'media')

"""
Aqui definiremos donde se encuentran nuestros archivos estaticos
"""

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
