"""
URL configuration for boutique_ado project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
# Importa el módulo 'admin' de Django para registrar las URLs del panel de administración.
from django.contrib import admin

# Importa la función 'path' y el módulo 'include' de Django para definir las URL y para incluir URLs de otras aplicaciones.
from django.urls import path, include

# Define las URLs del proyecto.
urlpatterns = [
    # Asocia la URL '/admin/' con las vistas del panel de administración de Django.
    path('admin/', admin.site.urls),

    # Asocia la URL '/accounts/' con las URLs relacionadas con la autenticación y registro de usuarios utilizando 'allauth'.
    path('accounts/', include('allauth.urls')),

    # Asocia la URL raíz '' con las URLs definidas en la aplicación 'home'.
    path('', include('home.urls')),
]

