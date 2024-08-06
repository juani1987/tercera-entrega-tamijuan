from typing import AbstractSet
from django.db import models

#Modelo de la aplicacion (negocio Tienda de Café)

class Cliente(models.Model): # modelo de clinte 
    first_name = models.CharField(max_length=100)  # Nombre del cliente
    last_name = models.CharField(max_length=100)   # Apellido del cliente
    email = models.EmailField()  
    def __str__(self): 
        return f'{self.first_name},{self.last_name},{self.email}' 
class Meta:
    verbose_name = "nombre"
    verbose_name_prural ="Nombres"
    ordenig =["nombre", "apellido"]

class Producto(models.Model): # modelo de listado de productos
    nombre = models.CharField(max_length=100)  # Nombre del producto
    descripcion = models.TextField()          # Descripción del producto
    precio = models.DecimalField(max_digits=10, decimal_places=2)  # Precio

    def __str__(self): #metodo str para mostrar al usuario la descripcion de su compra
        return f'{self.nombre},{self.descripcion},{self.precio}'
class Meta:
    verbose_name = "Producto"
    verbose_name_prural ="Productos"
    ordening =["producto", "descripcion"]

class Factura(models.Model): #modelo de facturación
    articulo = models.CharField(max_length=50) #Nombre del articulo Seleccionado
    fecha_de_emision = models.DateField()       #Fecha de Emisión De La Factura
    comprobante = models.CharField(max_length=50) #Comprobante de la Factura emitida
    
    def __str__(self): #metodo str para mostrar al usuario su facturación
        return f'{self.articulo},{self.comprobante},{self.fecha_de_emision},'

class Envio (models.Model): #modelo de envio de productos
    direccion = models.CharField(max_length=50) #Dirrecion del Remito 
    entregado = models.BooleanField()

    def __str__(self): #metodo str para mostrar el estado del envio
        return f'{self.direccion},{self.entregado}'

class Vendedor(models.Model): #Modelo de vendedor
    nombre = models.CharField(max_length=50) #Nombre de Vendedor
    apellido = models.CharField(max_length=50) #Apellido de Vendedor
    email = models.EmailField()                 #Email de Vendedor

class Pedido(models.Model):
    nombre_cliente = models.CharField(max_length=100)
    bebida = models.CharField(max_length=100)
    tamano = models.CharField(max_length=50)
    extras = models.TextField(blank=True)

    def __str__(self):
        return f"Tu Pedido {self.bebida}, {self.extras} esta esta en proceso , por favor {self.nombre_cliente} indicanos si queres agregar algo mas " 

class CustomUser(AbstractSet):
    username = models.CharField(max_length=150)
    email = models.EmailField()
    password1 = models.CharField(max_length=150)
    password2 = models.CharField(max_length=150) 
    last_name = models.CharField(max_length=150)
    first_name = models.CharField(max_length=150)
class Meta:
    verbose_name = "Usuario"
    verbose_name_prural ="Usuarios"
    ordening =["Usuario", "datos"]
  

   


class User (models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.BooleanField()




