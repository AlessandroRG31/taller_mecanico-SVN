from django import forms
from django.core.exceptions import ValidationError
from django.forms import inlineformset_factory
from datetime import date

from .models import Vehiculo, Mantenimiento, RepuestoMantenimiento
from clientes.models import Cliente


class VehiculoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cliente'].queryset = Cliente.objects.all()
        self.fields['cliente'].label_from_instance = lambda obj: f"{obj.nombre} – {obj.dui}"

    class Meta:
        model = Vehiculo
        fields = '__all__'
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-select'}),
            'placa': forms.TextInput(attrs={'class': 'form-control'}),
            'marca': forms.TextInput(attrs={'class': 'form-control'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control'}),
            'anio': forms.NumberInput(attrs={'class': 'form-control'}),
            'tipo': forms.TextInput(attrs={'class': 'form-control'}),
            'costo': forms.NumberInput(attrs={'class': 'form-control'}),
            'foto_placa': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'foto_frente': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'foto_frontal': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'foto_trasera': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'foto_lateral1': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'foto_lateral2': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

    def clean_costo(self):
        costo = self.cleaned_data.get('costo')
        if costo is not None and costo <= 0:
            raise ValidationError("El costo debe ser mayor que 0.")
        return costo


class MantenimientoForm(forms.ModelForm):
    class Meta:
        model = Mantenimiento
        fields = ['vehiculo', 'tipo_mantenimiento', 'fecha_mantenimiento', 'costo']
        widgets = {
            'vehiculo': forms.Select(attrs={'class': 'form-select'}),
            'tipo_mantenimiento': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_mantenimiento': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'costo': forms.NumberInput(attrs={'class': 'form-control'}),
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
        'cantidad': forms.NumberInput(attrs={'min': 1, 'class': 'form-control'}),
        'repuesto': forms.Select(attrs={'class': 'form-select'}),
    }
)
