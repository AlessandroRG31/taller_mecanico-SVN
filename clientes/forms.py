from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'nombre',
            'apellido',
            'dui',
            'licencia_conducir',
            'licencia_circulacion',
            'telefono',
            'direccion',
        ]
