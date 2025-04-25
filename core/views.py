from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required

def landing(request):
    """
    Página de bienvenida (landing page).
    """
    return render(request, 'core/landing.html')


def login_view(request):
    """
    Autenticación de usuarios.
    - GET: muestra el formulario.
    - POST: valida credenciales e inicia sesión.
    """
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()

    return render(request, 'core/login.html', {'form': form})


def register_view(request):
    """
    Registro de nuevos usuarios.
    - GET: muestra UserCreationForm.
    - POST: crea el usuario y redirige al login.
    """
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'core/register.html', {'form': form})


@login_required
def dashboard(request):
    """
    Panel principal tras login.
    """
    return render(request, 'core/dashboard.html')


@login_required
def logout_view(request):
    """
    Cierra la sesión y redirige a landing.
    """
    logout(request)
    return redirect('landing')
