from django import forms
from .models import Cliente
from mantenimiento.models import Vehiculo

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

class VehiculoForm(forms.ModelForm):
    """
    Formulario para crear Vehículo desde la app Clientes.
    Incluye FK a Cliente y el resto de campos básicos.
    """
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
        # Sin widgets de Select2 ni JS de autocompletado
