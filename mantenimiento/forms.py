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
        fields = '__all__'
        widgets = {
            'fecha_proxima_revision': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_cliente(self):
        cliente = self.cleaned_data.get('cliente')
        if not cliente:
            raise ValidationError("Debe seleccionar un cliente.")
        return cliente

    def clean_costo(self):
        costo = self.cleaned_data.get('costo')
        if costo is not None and costo <= 0:
            raise ValidationError("El costo debe ser mayor que cero.")
        return costo

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
    widgets={'cantidad': forms.NumberInput(attrs={'min': 1})},
)
