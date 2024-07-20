from shutil import register_archive_format
from typing import Self
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from.moduls import*
from django.shortcuts import render, redirect
from django.contrib.auth.models import User


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
def updateClinte(request, id_cliente):
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
def deleteClinte(request, id_cliente):
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
  # Asegúrate de importar tu formulario de registro adecuadamente

def register(request):
    if request.method == "POST":
        myForm = RegisterForm(request.POST)
        if myForm.is_valid():
            username = myForm.cleaned_data.get("username")
            if User.objects.filter(username=username).exists():
                myForm.add_error("username", "Nombre de usuario no disponible.")
            else:
                myForm.save()
                # Redirige a la página de éxito 
                return redirect("misdatos/index.html")  
    else:
        myForm = RegisterForm()
    
    return render(request, "misdatos/registro.html", {"form": myForm})


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

