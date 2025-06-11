# taller_mecanico-SVN-main/mantenimiento/forms.py

from django import forms
from django.core.exceptions import ValidationError
from django.forms import inlineformset_factory
from .models import Vehiculo, Mantenimiento, RepuestoMantenimiento
from clientes.models import Cliente

class VehiculoForm(forms.ModelForm):
    cliente = forms.ModelChoiceField(
        queryset=Cliente.objects.all(),
        label="Cliente",
        error_messages={'required': 'Debe seleccionar un cliente.'}
    )

    class Meta:
        model = Vehiculo
        fields = [
            'cliente', 'placa', 'marca', 'modelo', 'anio', 'tipo',
            'costo', 'foto_frente', 'foto_trasera', 'foto_lateral1', 'foto_lateral2',
            'fecha_proxima_revision'
        ]
        widgets = {
            'fecha_proxima_revision': forms.DateInput(attrs={'type': 'date'})
        }

    def clean_cliente(self):
        cliente = self.cleaned_data.get('cliente')
        if not cliente:
            raise ValidationError("Debe seleccionar un cliente.")
        return cliente

    def clean_costo(self):
        costo = self.cleaned_data.get('costo')
        if costo is None or costo <= 0:
            raise ValidationError("El costo debe ser mayor que cero.")
        return costo

class MantenimientoForm(forms.ModelForm):
    class Meta:
        model = Mantenimiento
        fields = ['vehiculo', 'fecha_mantenimiento', 'costo']
        widgets = {
            'fecha_mantenimiento': forms.DateInput(attrs={'type': 'date'})
        }

RepuestoMantenimientoFormSet = inlineformset_factory(
    Mantenimiento,
    RepuestoMantenimiento,
    fields=('repuesto', 'cantidad'),
    extra=1,
    can_delete=True,
    widgets={'cantidad': forms.NumberInput(attrs={'min': 1})}
)
