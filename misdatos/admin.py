from django.contrib import admin
from misdatos.moduls import *
from misdatos.moduls import Vendedor

class VendedorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'email')  # Ajusta según los campos correctos de tu modelo Vendedor

admin.site.register(Cliente)
admin.site.register(Vendedor, VendedorAdmin)
admin.site.register(Producto)
admin.site.register(Factura)
admin.site.register(Envio) 
 


