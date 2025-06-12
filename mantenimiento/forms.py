from django import forms
from django.forms import inlineformset_factory

from .models import Vehiculo, Mantenimiento, RepuestoMantenimiento

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = [
            'cliente',
            'placa',
            'marca',
            'modelo',
            'anio',
            'tipo',
            'costo',
            'foto_frente',
            'foto_trasera',
            'foto_lateral1',
            'foto_lateral2',
            'fecha_proxima_revision',
        ]

class MantenimientoForm(forms.ModelForm):
    class Meta:
        model = Mantenimiento
        fields = [
            'vehiculo',
            'tipo_mantenimiento',
            'fecha_mantenimiento',
            'costo',
        ]
        widgets = {
            'fecha_mantenimiento': forms.DateInput(attrs={'type': 'date'}),
        }

RepuestoMantenimientoFormSet = inlineformset_factory(
    Mantenimiento,
    RepuestoMantenimiento,
    fields=('repuesto', 'cantidad'),
    extra=1,
    can_delete=True,
    widgets={'cantidad': forms.NumberInput(attrs={'min': 1})}
)
