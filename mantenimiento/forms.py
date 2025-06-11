from django import forms
from .models import Vehiculo, Mantenimiento, RepuestoMantenimiento
from django.forms import inlineformset_factory

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = [
            'cliente',
            'placa', 'marca', 'modelo', 'anio',
            'tipo', 'costo',
            'foto_frente', 'foto_trasera',
            'foto_lateral1', 'foto_lateral2',
            'fecha_proxima_revision',
        ]
        widgets = {
            # dejamos el select por defecto de Django
            # si quisieras, podrías personalizar attrs={'class': 'form-control'}, etc.
        }

class MantenimientoForm(forms.ModelForm):
    class Meta:
        model = Mantenimiento
        fields = ['vehiculo', 'fecha_mantenimiento', 'costo']
        widgets = {
            'fecha_mantenimiento': forms.DateInput(attrs={'type': 'date'}),
        }

RepuestoMantenimientoFormSet = inlineformset_factory(
    Mantenimiento,
    RepuestoMantenimiento,
    fields=('repuesto', 'cantidad'),
    extra=1,
    can_delete=True,
    widgets={
        'cantidad': forms.NumberInput(attrs={'min': 1}),
    }
)
