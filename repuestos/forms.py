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
        labels = {
            'empresa': 'Empresa vendedora',
            'nombre': 'Nombre del repuesto',
            'precio': 'Precio (S/.)',
            'stock': 'Stock disponible',
        }
