from django.contrib import admin
from .models import Vehiculo, Mantenimiento, RepuestoMantenimiento

@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
    list_display = ('placa', 'marca', 'modelo', 'cliente')
    search_fields = ('placa', 'marca', 'modelo')

@admin.register(Mantenimiento)
class MantenimientoAdmin(admin.ModelAdmin):
    list_display = ('vehiculo', 'tipo_mantenimiento', 'fecha_mantenimiento', 'costo')
    list_filter = ('tipo_mantenimiento',)
    date_hierarchy = 'fecha_mantenimiento'

@admin.register(RepuestoMantenimiento)
class RepuestoMantenimientoAdmin(admin.ModelAdmin):
    list_display = ('mantenimiento', 'repuesto', 'cantidad')
    list_filter = ('repuesto',)
