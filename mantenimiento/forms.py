from django import forms
from .models import Vehiculo, Mantenimiento

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['cliente', 'placa', 'modelo', 'anio']
        # Sin widgets externos: dejamos el select nativo de ModelChoiceField

class MantenimientoForm(forms.ModelForm):
    class Meta:
        model = Mantenimiento
        fields = ['vehiculo', 'tipo_mantenimiento', 'fecha_mantenimiento', 'costo']
        widgets = {
            'fecha_mantenimiento': forms.DateInput(attrs={'type': 'date'}),
        }
