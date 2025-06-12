# clientes/forms.py
from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'dui', 'telefono', 'email', 'direccion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'dui': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '12345678-9'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '7777-7777'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'direccion': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        }
