"""
URL configuration for sap project.

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
from django.urls import path, include
from misdatos.views import *


urlpatterns = [
    path('', inicio, name="inicio"),
    path('productos/', productos, name="products"),
    path('about/', acercade, name="acercade"),
    path('store/', tienda, name="tienda"),
    path('index/', inicio, name="home"),
    #Formulario  
    path('formulario/', tusdatos, name='tusdatos'),
    path('clinteform/', clinte, name="clinte" ),
    path('update_profesor/<id_profesor>/', updateClinte, name="update_Clinte" ),
    path('delete_profesor/<id_profesor>/', deleteClinte, name="delete_Clinte" ),
    path('create_profesor/', createClinte, name="create_Clinte" ),  
    #Funcion Busqueda
    path('buscarProductos', buscarProducto , name ="buscar"),
    path('buscar2/', buscar2, name="buscar"),
    path('register',register,name= "register")  
]

