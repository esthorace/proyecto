from django.contrib import admin

from . import models

# admin.site.register(models.Pais)
# admin.site.register(models.Cliente)


@admin.register(models.Pais)
class PaisAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)
    ordering = ('nombre',)


@admin.register(models.Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'nacimiento', 'pais_origen_id')
    search_fields = ('nombre', 'apellido')
    ordering = ('apellido', 'nombre')
    list_filter = ('pais_origen_id',)
    date_hierarchy = 'nacimiento'
