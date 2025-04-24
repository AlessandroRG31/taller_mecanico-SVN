from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label="Nombre de usuario",
        min_length=4, max_length=150,
        help_text="4–150 caracteres. Letras, dígitos y @/./+/-/_ solamente.",
        validators=[RegexValidator(r'^[\w.@+-]+$', "Solo letras, dígitos y @/./+/-/_")]
    )
    password1 = forms.CharField(
        label="Contraseña",
        strip=False,
        widget=forms.PasswordInput,
        help_text="Mínimo 8 caracteres, 1 mayúscula, 1 dígito y 1 símbolo."
    )
    password2 = forms.CharField(
        label="Confirmación",
        strip=False,
        widget=forms.PasswordInput,
        help_text="Repite la misma contraseña."
    )

    class Meta:
        model  = User
        fields = ["username", "password1", "password2"]

    def clean_password1(self):
        pwd = self.cleaned_data.get("password1", "")
        if len(pwd) < 8:
            raise forms.ValidationError("Al menos 8 caracteres.")
        if not any(c.isupper() for c in pwd):
            raise forms.ValidationError("Debe tener una mayúscula.")
        if not any(c.isdigit() for c in pwd):
            raise forms.ValidationError("Debe tener un dígito.")
        if not any(c in "!@#$%^&*()_+-=[]{}|;':\",.<>/?`~" for c in pwd):
            raise forms.ValidationError("Debe tener un símbolo.")
        return pwd
