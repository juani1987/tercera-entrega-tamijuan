from msilib.schema import ListView
from shutil import register_archive_format
from typing import Self
from winreg import CreateKey
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from.moduls import*
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm

from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import PasswordChangeView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from misdatos.forms import AvatarForm



from.forms import *

def inicio(request):
    return render(request, "misdatos/index.html")

def productos(request):
    contexto = {"producto": Producto.objects.all()}
    return render(request, "misdatos/products.html", contexto)

def acercade(request):
    return render(request, "misdatos/about.html")

def tienda (request):
    contexto = {"producto": Producto.objects.all()}
    return render(request, "misdatos/store.html",contexto)

def clinteForm(request):
    if request.method == "POST":
        clinte = Cliente(nombre=request.POST['nombre'], 
                      comision=request.POST['apellido'])
        clinte.save()
        return HttpResponse("Se grabo con exito el curso!")
    
    return render(request, "aplicacion/clintesform.html")
# Formulario Clinte
def tusdatos(request):
    if request.method == "POST":
        miForm = ClienteForm(request.POST)
        if miForm.is_valid():
            clinte_first_name = miForm.cleaned_data.get('first_name')
            clinte_last_name = miForm.cleaned_data.get('last_name')
            clinte_email = miForm.cleaned_data.get("email")
            clinte = Cliente(first_name= clinte_first_name,
                          last_name = clinte_last_name,
                          email = clinte_email )
            clinte.save()
            return render(request, "misdatos/index.html")
    else:
        miForm = ClienteForm()

    return render(request, "misdatos/formulario.html", {"form": miForm })

#Crear Usuario def Clinte(request):
def clinte(request):
    ctx = {'clinte': Cliente.objects.all()}
    return render(request, "misdatos/clintesform.html", ctx)
#Clinte Update
def updateCliente(request, id_cliente):
    clinte = Cliente.objects.get(id=id_cliente)
    if request.method == "POST":
        miForm = ClienteForm(request.POST)
        if miForm.is_valid():
            clinte.nombre = miForm.cleaned_data.get('first_name')
            clinte.apellido = miForm.cleaned_data.get('last_name')
            clinte.email = miForm.cleaned_data.get('email')
        
            clinte.save()
            return redirect(reverse_lazy('clinte'))   
    else:
        miForm = ClienteForm(initial={
            'nombre': clinte.nombre,
            'apellido': clinte.apellido,
            'email': clinte.email,
        })
    return render(request, "misdatos/clintesform.html", {'form': miForm})

#CRUD CLIENTE
def deleteCliente(request, id_cliente):
    cliente= Cliente.objects.get(id=id_cliente)
    cliente.delete()
    return redirect(reverse_lazy('clinte'))

def createClinte(request):    
    if request.method == "POST":
        miForm = ClienteForm(request.POST)
        if miForm.is_valid():
            p_nombre = miForm.cleaned_data.get('nombre')
            p_apellido = miForm.cleaned_data.get('apellido')
            p_email = miForm.cleaned_data.get('email')
            clinte = Cliente(nombre=p_nombre, 
                             apellido=p_apellido,
                             email=p_email)
            clinte.save()
            return redirect(reverse_lazy('clinte'))
    else:
        miForm = ClienteForm()

    return render(request, "misdatos/formulario.html", {"form":miForm})

# loging clinte 
#Para el login

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate 

@login_required
def nuevoclinte(request):
    contexto = {"clinte": Cliente.objects.all()}
    return render(request, "misdatos/clinte.html", contexto)

@login_required
def clinteForm(request):
    if request.method == "POST":
        miForm = ClienteForm(request.POST)
        if miForm.is_valid():
            nombre = miForm.cleaned_data.get("nombre")
            apellido = miForm.cleaned_data.get("apellido")
            cliente = Cliente(first_name= nombre, last_name = apellido)
            cliente.save()
            contexto = {"clintes": Cliente.objects.all() }
            return render(request, "misdatos/clinte.html", contexto)
    else:
        miForm = clinteForm()
    
    return render(request, "entidades/cursoForm.html", {"form": miForm})

@login_required
def clinteUpdate(request, id_curso):
    cliente = Cliente.objects.get(id=id_curso)
    if request.method == "POST":
        miForm = ClienteForm(request.POST)
        if miForm.is_valid():
            cliente.nombre= miForm.cleaned_data.get("nombre")
            cliente.apellido = miForm.cleaned_data.get("apellido")
            cliente.save()
            contexto = {"cliente": Cliente.objects.all() }
            return render(request, "misdatos/clintes.html", contexto)       
    else:
        miForm = ClienteForm(initial={"nombre": cliente.nombre, "apellido":  cliente.apellido}) 
    
    return render(request, "misdatos/clintesform.html", {"form": miForm})

@login_required
def clinteDelete(request, id_curso):
    clinte = Cliente.objects.get(id=id_curso)
    clinte.delete()
    contexto = {"clinte": Cliente.objects.all() }
    return render(request, "misdatos/clintes.html", contexto)     
#class ClientesList(LoginRequiredMixin, ListView):
   # model = Cliente

#lass createClinte (LoginRequiredMixin, CreateView):
    #model = Cliente
   # fields = ["nombre", "apellido", "email"]
   ## success_url = reverse_lazy("estudiantes")

#class updateCliente (LoginRequiredMixin, UpdateView):
   # model = Cliente
    ##fields = ["nombre", "apellido", "email"]
   # success_url = reverse_lazy("estudiantes")

#class deleteCliente (LoginRequiredMixin, DeleteView):
   # model = Cliente
    #success_url = reverse_lazy("estudiantes")


def loginRequest(request):
    if request.method == "POST":
        usuario = request.POST["username"]
        clave = request.POST["password"]
        user = authenticate(request, username=usuario, password=clave)
        if user is not None:
            login(request, user)

            #_______ Buscar Avatar
            try:
                avatar = avatar.objects.get(user=request.user.id).imagen.url
            except:
                avatar = "/media/avatares/default.png"
            finally:
                request.session["avatar"] = avatar
            #______________________________________________________________
            return render(request, "misdatos/index.html")
        else:
            return redirect(reverse_lazy('login'))

    else:
        miForm = AuthenticationForm()

    return render(request, "misdatos/login.html", {"form": miForm})

def register(request):
    if request.method == "POST":
        miForm = RegistroForm(request.POST)
        if miForm.is_valid():
            #usuario = miForm.cleaned_data.get("username")
            miForm.save()
            return redirect(reverse_lazy('home'))
    else:
        miForm = RegistroForm()

    return render(request, "misdatos/registro.html", {"form": miForm})   
# Edicion de perfil y Avatar

def editPerfil(request):
    usuario = request.user 
    if request.method == "POST":
        miForm = UserEditForm(request.POST)
        if miForm.is_valid():
            user = User.objects.get(username = usuario )
            user.email = miForm.cleaned_data.get ("email")
            user.nombre = miForm.cleaned_data.get("nombre")
            user.apellido = miForm.changed_data.get("apellido")
            user.save()
        return redirect (reverse_lazy ("index"))
    else: 
        miForm = UserEditForm (isinstance= usuario)
    return request ("misdatos/editarPerfil.html", {"form": miForm})

def inicio(request):

      avatares = Avatar.objects.filter(user=request.user.id)
      
      return render(request, "misdatos/index.html", {"url":avatares[0].imagen.url})

def agregarAvatar(request):
    if request.method == "POST":
        miForm = AvatarForm(request.POST, request.FILES)
        if miForm.is_valid():
            usuario = User.objects.get(username=request.user)
            imagen = miForm.cleaned_data["imagen"]
            #_________ Borrar avatares viejos
            avatarViejo = Avatar.objects.filter(user=usuario)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()
            #__________________________________________
            avatar = Avatar(user=usuario, imagen=imagen)
            avatar.save()

            #_________ Enviar la imagen al home
            imagen = Avatar.objects.get(user=usuario).imagen.url
            request.session["avatar"] = imagen
            #____________________________________________________
            return redirect(reverse_lazy("home"))
    else:
        miForm = AvatarForm()
    return render(request, "entidades/agregarAvatar.html", {"form": miForm})    

def cliente (request):

      return render(request, "misdatos/clientes.html")
# Busqueda De Productos 
def buscarProducto(request):
    return render(request, "misdatos/buscar.html")
def buscar2(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        productos = Producto.objects.filter(nombre__icontains=patron)
        contexto = {"producto": productos, 'titulo': f'Producto que tiene como patron "{patron}"'}
        return render(request, "misdatos/products.html", contexto)
    return HttpResponse("No se ingreso nada a buscar")

