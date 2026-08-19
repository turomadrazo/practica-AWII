from django.contrib import admin

# Register your models here.
from .models import Producto, Pedido

admin.site.site_header = "Admon Cafeturo"
admin.site.site_title = "Panel Cafeturo"
admin.site.index_title = "Bienvenido al Panel de Administración de Cafeturo"

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'precio', 'categoria', 'disponible')
    list_filter = ('categoria', 'disponible')
    search_fields = ('nombre',)

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente_nombre', 'estado', 'total', 'fecha')
    list_filter = ('estado', 'fecha')
    search_fields = ('cliente_nombre',)