from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    """
    Formulario de Cliente: incluye todos los campos del modelo
    y usa el select nativo de Django para cualquier FK.
    """
    class Meta:
        model = Cliente
        fields = '__all__'
