from typing import Self
from django.http import HttpResponse
from django.shortcuts import redirect, render
from.moduls import*

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
    
    return render(request, "aplicacion/cursoForm.html")

def tusdatos(request):
    if request.method == "POST":
        miForm = ClienteForm(request.POST)
        if miForm.is_valid():
            clinte_nombre = miForm.cleaned_data.get('nombre')
            clinte_apellido = miForm.cleaned_data.get('apellido')
            clinte = Cliente(nombre=clinte_nombre,
                          apellido= clinte_apellido)
            clinte.save()
            return render(request, "formulario.html")
    else:
        miForm = ClienteForm()
    
    return render(request, "formulario.html", {"form": miForm })

def buscarProducto(request):
    return render(request, "misdatos/products.html")

def buscar2(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        productos = Producto.objects.filter(nombre__icontains=patron)
        contexto = {"producto": productos, 'titulo': f'Producto que tiene como patron "{patron}"'}
        return render(request, "misdatos/products.html", contexto)
    return HttpResponse("No se ingreso nada a buscar")