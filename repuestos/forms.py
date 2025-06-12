from django import forms
from .models import Empresa, Repuesto

class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ['nombre', 'telefono']
        labels = {
            'nombre': 'Nombre de la empresa',
            'telefono': 'Teléfono',
        }

class RepuestoForm(forms.ModelForm):
    class Meta:
        model = Repuesto
        fields = ['empresa', 'nombre', 'precio', 'stock']
        widgets = {
            'empresa': forms.Select(attrs={'class': 'form-select'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
        }




