# repuestos/admin.py

from django.contrib import admin
from .models import Empresa, Repuesto

@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display  = ("nombre", "telefono")
    search_fields = ("nombre",)

@admin.register(Repuesto)
class RepuestoAdmin(admin.ModelAdmin):
    list_display  = ("nombre", "empresa", "precio", "stock")
    list_filter   = ("empresa",)
    search_fields = ("nombre",)
