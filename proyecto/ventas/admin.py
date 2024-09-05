from django.contrib import admin

from .models import Vendedor, Venta

admin.site.register(Vendedor)


@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ('vendedor', 'producto', 'cantidad', 'precio_total', 'fecha_venta')
    list_display_links = ('producto',)
    search_fields = ('producto.nombre', 'vendedor.nombre', 'vendedor.apellido')
    list_filter = ('vendedor',)
    date_hierarchy = 'fecha_venta'
