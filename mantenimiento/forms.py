from django import forms
from .models import Vehiculo, Mantenimiento

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = [
            'placa', 'marca', 'modelo', 'anio', 'tipo', 'costo',
            'foto_frente', 'foto_trasera', 'foto_lateral1', 'foto_lateral2',
            'fecha_proxima_revision'
        ]
        widgets = {
            'fecha_proxima_revision': forms.DateInput(attrs={'type': 'date'}),
        }

class MantenimientoForm(forms.ModelForm):
    class Meta:
        model = Mantenimiento
        fields = [
            'vehiculo', 'tipo_mantenimiento', 'fecha_mantenimiento', 'costo'
        ]
        widgets = {
            'fecha_mantenimiento': forms.DateInput(attrs={'type': 'date'}),
        }
