from django import forms
from django.core.exceptions import ValidationError
from django.forms import inlineformset_factory

from .models import Vehiculo, Mantenimiento, RepuestoMantenimiento
from clientes.models import Cliente

class VehiculoForm(forms.ModelForm):
    cliente = forms.ModelChoiceField(
        queryset=Cliente.objects.all(),
        label="Cliente",
        error_messages={'required': 'Debe seleccionar un cliente.'},
        widget=forms.Select(
            attrs={
                'class': 'select2',
                'data-placeholder': 'Seleccione un cliente'
            }
        )
    )

    class Meta:
        model = Vehiculo
        fields = '__all__'


class MantenimientoForm(forms.ModelForm):
    class Meta:
        model = Mantenimiento
        fields = ['vehiculo', 'fecha_mantenimiento', 'costo']
        widgets = {
            'vehiculo': forms.Select(
                attrs={
                    'class': 'select2',
                    'data-placeholder': 'Seleccione un vehículo'
                }
            ),
            'fecha_mantenimiento': forms.DateInput(
                attrs={'type': 'date'}
            ),
        }

    def clean_costo(self):
        costo = self.cleaned_data.get('costo')
        if costo is not None and costo <= 0:
            raise ValidationError("El costo del mantenimiento debe ser mayor que 0.")
        return costo


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
