from django import forms
from django.forms import inlineformset_factory

from .models import Vehiculo, Mantenimiento, RepuestoMantenimiento
from clientes.models import Cliente

class VehiculoForm(forms.ModelForm):
    cliente = forms.ModelChoiceField(
        queryset=Cliente.objects.all(),
        empty_label="— Selecciona un cliente —",
        label="Cliente",
        error_messages={'required': 'Debe seleccionar un cliente.'}
    )

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
        # Sin widgets de autocompletar externos; usamos el select nativo

class MantenimientoForm(forms.ModelForm):
    # Campo vehiculo como ModelChoiceField nativo
    vehiculo = forms.ModelChoiceField(
        queryset=Vehiculo.objects.all(),
        empty_label="— Selecciona un vehículo —",
        label="Vehículo",
        error_messages={'required': 'Debe seleccionar un vehículo.'}
    )

    class Meta:
        model = Mantenimiento
        fields = ['vehiculo', 'fecha_mantenimiento', 'costo']
        widgets = {
            'fecha_mantenimiento': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_costo(self):
        costo = self.cleaned_data.get('costo')
        if costo is not None and costo <= 0:
            raise forms.ValidationError("El costo del mantenimiento debe ser mayor que 0.")
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
