# ruta: taller_mecanico/core/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required

def landing(request):
    return render(request, 'core/home.html')

def login_view(request):
    if request.user.is_authenticated:
        return redirect('core:dashboard')
    error = None
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('core:dashboard')
        error = "Usuario o contraseña inválidos."
    else:
        form = AuthenticationForm()
    return render(request, 'core/login.html', {'form': form, 'error': error})

def register_view(request):
    if request.user.is_authenticated:
        return redirect('core:dashboard')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect('core:dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'core/register.html', {'form': form})

@login_required
def dashboard(request):
    return render(request, 'core/dashboard.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('core:landing')
