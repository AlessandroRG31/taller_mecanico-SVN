from django.contrib import admin
from .models import Vehiculo, Mantenimiento, RepuestoMantenimiento

class RepuestoMantenimientoInline(admin.TabularInline):
    model = RepuestoMantenimiento
    extra = 1  # permite añadir repuestos

@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
    list_display = ('placa', 'marca', 'modelo', 'cliente')
    search_fields = ('placa', 'marca', 'modelo', 'cliente__nombre')
    list_filter = ('marca', 'cliente')

@admin.register(Mantenimiento)
class MantenimientoAdmin(admin.ModelAdmin):
    list_display = ('id', 'vehiculo', 'fecha_mantenimiento', 'costo')
    list_filter = ('fecha_mantenimiento',)
    search_fields = ('vehiculo__placa',)
    inlines = [RepuestoMantenimientoInline]

@admin.register(RepuestoMantenimiento)
class RepuestoMantenimientoAdmin(admin.ModelAdmin):
    list_display = ('mantenimiento', 'repuesto', 'cantidad')
    search_fields = ('repuesto__nombre',)
