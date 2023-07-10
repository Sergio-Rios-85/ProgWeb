from django.contrib import admin

from gestionPedido.models import Cliente,Articulos,Pedidos

class ClienteAdmin(admin.ModelAdmin):
    list_display=("nombre","diereccion","email")
    search_fields=("nombre","email")

class ArticulosAdmin(admin.ModelAdmin):
    list_display=("nombre","seccion","precio")
    list_filter=("seccion",)

class PedidosAdmin(admin.ModelAdmin):
    list_display=("numero", "fecha")  
    list_filter=("fecha",)  
    date_hierarchy="fecha"

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Articulos, ArticulosAdmin)
admin.site.register(Pedidos, PedidosAdmin)
