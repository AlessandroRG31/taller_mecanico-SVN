from django.contrib import admin
from .models import Vehiculo, ProximoMantenimiento, Mantenimiento

class ProximoMantenimientoInline(admin.TabularInline):
    model = ProximoMantenimiento
    extra = 2  # cuántas fechas permitir añadir por defecto

@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
    list_display   = ['placa', 'cliente', 'marca', 'modelo', 'anio', 'tipo', 'costo']
    list_filter    = ['tipo', 'anio']
    search_fields  = ['placa', 'cliente', 'marca', 'modelo']
    inlines        = [ProximoMantenimientoInline]

@admin.register(Mantenimiento)
class MantenimientoAdmin(admin.ModelAdmin):
    list_display      = ['vehiculo', 'tipo_mantenimiento', 'fecha_mantenimiento', 'costo']
    list_filter       = ['tipo_mantenimiento', 'fecha_mantenimiento']
    search_fields     = ['vehiculo__placa', 'tipo_mantenimiento']
    filter_horizontal = ['repuestos']
