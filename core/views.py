# core/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required

# Vista de inicio (home)
def landing(request):
    # Cambiado de 'core/landing.html' a 'core/home.html'
    return render(request, 'core/home.html')

# Iniciar sesión
def login_view(request):
    if request.user.is_authenticated:
        return redirect('core:dashboard')
    error = None
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('core:dashboard')
        else:
            error = 'Usuario o contraseña incorrectos'
    else:
        form = AuthenticationForm()
    return render(request, 'core/login.html', {'form': form, 'error': error})

# Registro de usuario
def register_view(request):
    if request.user.is_authenticated:
        return redirect('core:dashboard')
    error = None
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:login')
        else:
            error = 'Error al crear la cuenta'
    else:
        form = UserCreationForm()
    return render(request, 'core/register.html', {'form': form, 'error': error})

# Dashboard de usuario autenticado
@login_required
def dashboard(request):
    return render(request, 'core/dashboard.html')

# Cerrar sesión
@login_required
def logout_view(request):
    logout(request)
    return redirect('core:landing')
