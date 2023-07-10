from django.contrib import admin
from .models import Cliente,Articulo,Pedido,Servicio

class ClienteAdmin(admin.ModelAdmin):
    list_display=("nombre","direccion","email")
    search_fields=("nombre","email")

class ArticuloAdmin(admin.ModelAdmin):
    list_filter=("seccion",)

class PedidoAdmin(admin.ModelAdmin):
    list_display=("numero", "fecha")  
    list_filter=("fecha",)  
    date_hierarchy="fecha"

class ServicioAmin(admin.ModelAdmin):
    readonly_fields=('created','updated')    

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Articulo, ArticuloAdmin)
admin.site.register(Pedido, PedidoAdmin)
admin.site.register(Servicio, ServicioAmin)
