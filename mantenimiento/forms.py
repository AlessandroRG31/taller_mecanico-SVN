from django import forms
from .models import Vehiculo, Mantenimiento
from clientes.models import Cliente

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Asegura que siempre se muestren todos los clientes disponibles
        self.fields['cliente'].queryset = Cliente.objects.all()
        # El campo cliente debe ser obligatorio
        self.fields['cliente'].required = True

class MantenimientoForm(forms.ModelForm):
    class Meta:
        model = Mantenimiento
        fields = '__all__'
