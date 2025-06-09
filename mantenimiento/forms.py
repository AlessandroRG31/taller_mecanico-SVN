from django import forms
from django.core.exceptions import ValidationError
from django.forms import inlineformset_factory
from dal import autocomplete
from datetime import date

from .models import Vehiculo, ProximoMantenimiento, Mantenimiento, RepuestoMantenimiento

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
            'foto_placa',
            'foto_frente',
            'foto_trasera',
            'foto_lateral1',
            'foto_lateral2',
        ]
        widgets = {
            'cliente': autocomplete.ModelSelect2(
                url='clientes:cliente-autocomplete'
            ),
        }

    def clean_costo(self):
        costo = self.cleaned_data.get('costo')
        if costo is not None and costo <= 0:
            raise ValidationError("El costo debe ser mayor que 0.")
        return costo

class ProximoMantenimientoForm(forms.ModelForm):
    class Meta:
        model = ProximoMantenimiento
        fields = ['fecha_programada']
        widgets = {
            'fecha_programada': forms.DateInput(attrs={'type': 'date'})
        }

    def clean_fecha_programada(self):
        fecha = self.cleaned_data.get('fecha_programada')
        if fecha and fecha <= date.today():
            raise ValidationError("La fecha programada debe ser posterior a hoy.")
        return fecha

class MantenimientoForm(forms.ModelForm):
    class Meta:
        model = Mantenimiento
        fields = [
            'vehiculo',
            'tipo_mantenimiento',
            'fecha_mantenimiento',
            'costo'
        ]
        widgets = {
            'fecha_mantenimiento': forms.DateInput(attrs={'type': 'date'}),
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
    widgets={'cantidad': forms.NumberInput(attrs={'min': 1})},
)
