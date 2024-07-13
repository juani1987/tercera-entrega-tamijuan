from django.db import models


# modelo de negocio de la app

class Modelo(models.Model):
    nombre = models.CharField(max_length=50)
    modelo = models.IntegerField()


class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    dni = models.CharField(max_length=50)


class Cacrrito(models.Model):
    producto = models.CharField(max_length=50)
    Estado = models.DateField()
    comprobante = models.CharField(max_length=50)
    verifiacion = models.BooleanField()


class Productos(models.Model):
    articulo = models.CharField(max_length=50)
    caracteristicas = models.CharField(max_length=50)
    stock = models.DateField()


class Comprobante(models.Model):
    emicion = models.TimeField
    factura = models.DateField
    datos = models.CharField(max_length=50)
