# mantenimiento/admin.py

from django.contrib import admin
from .models import Vehiculo, Mantenimiento, RepuestoMantenimiento

class RepuestoMantenimientoInline(admin.TabularInline):
    model = RepuestoMantenimiento
    extra = 1  # al menos una línea para cantidad de repuesto

@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
    list_display = ['placa', 'cliente', 'marca', 'modelo', 'anio', 'tipo', 'costo']
    list_filter = ['tipo', 'anio']
    search_fields = ['placa', 'cliente', 'marca', 'modelo']
    # inlines eliminado porque ProximoMantenimiento fue removido

@admin.register(Mantenimiento)
class MantenimientoAdmin(admin.ModelAdmin):
    list_display = ['vehiculo', 'tipo_mantenimiento', 'fecha_mantenimiento', 'costo']
    list_filter = ['tipo_mantenimiento', 'fecha_mantenimiento']
    search_fields = ['vehiculo__placa', 'tipo_mantenimiento']
    inlines = [RepuestoMantenimientoInline]
