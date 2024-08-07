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
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', inicio, name="inicio"),
    path('productos/', productos, name="products"),
    path('about/', acercade, name="acercade"),
    path('store/', tienda, name="tienda"),
    path('index/', inicio, name="home"),
    #Formulario  
    path('formulario/', tusdatos, name='tusdatos'),
    path('clienteform/', clinte, name="cliente" ),
    path('update_Clinte/<id_cliente>/', updateCliente, name="updateCliente" ),
    path('delete_Clinte/<id_cliente>/', deleteCliente, name="delete_Cliente" ),
    path('create_clinte/', createClinte, name="create_Clinte" ),  
    path('buscarProductos', buscarProducto , name ="buscar"),
 #Crud cliente
    #path('Clientes/', ClientesList.as_view(), name="Cliente"),    
   # path('clienteCreate/', createClinte.as_view(), name="clienteCreate"), 
    #path('clienteUpdate/<int:pk>/', updateCliente.as_view(), name="clienteUpdate"), 
    # path('clinteDelete/<int:pk>/', clinteDelete.as_view(), name="clienteDelete"), 
#buscador
    path('buscar2/', buscar2, name="buscar"),
    path('register',register,name= "register"), 
#Loging/Logout
    path('login/', loginRequest, name="login"),
    path('logout/', LogoutView.as_view(template_name="entidades/logout.html"), name="logout"),
    path('registro/', register, name="registro"),
    

]

