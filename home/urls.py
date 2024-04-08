from django.contrib import admin
from django.urls import path

# necesito importar las views
from . import views

# Importa las vistas definidas en el archivo 'views.py' de la aplicación actual.


# Define las URLs del proyecto.
urlpatterns = [
    # Asocia la URL raíz '' con la vista 'index' definida en 'views.py', y le asigna el nombre 'home'.
    path('', views.index, name='home')
]
