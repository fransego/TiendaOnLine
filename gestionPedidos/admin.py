from django.contrib import admin
from gestionPedidos.models import Clientes, Articulos, Pedidos

# Register your models here.

class ClientesAdmin(admin.ModelAdmin):
    #agrega campos a la vista clientes
    list_display=("nombre","direccion","telefono")

    #agregar busqueda de clientes
    search_fields=("nombre","telefono")

class ArticulosAdmin(admin.ModelAdmin):
    #agrega un filtro a la vista Articulos
    list_filter=("seccion",)

class PedidosAdmin(admin.ModelAdmin):
    #agrega campos a la vista Pedidos
    list_display=("numero","fecha")

     #agrega un filtro a la vista Pedidos
    list_filter=("fecha",)

    date_hierarchy="fecha"

admin.site.register(Clientes, ClientesAdmin)
admin.site.register(Articulos, ArticulosAdmin)
admin.site.register(Pedidos, PedidosAdmin)