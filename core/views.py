from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required

def landing(request):
    """
    Página de bienvenida. Muestra la plantilla home.html.
    """
    return render(request, 'core/home.html')

def login_view(request):
    """
    Gestiona el inicio de sesión:
    - Si el usuario ya está autenticado, lo redirige al dashboard.
    - Con GET muestra el formulario de autenticación.
    - Con POST valida credenciales y, si son correctas, inicia sesión y redirige al dashboard.
    - Si falla, vuelve a mostrar login.html con mensaje de error.
    """
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
        error = "Usuario o contraseña inválidos."
    else:
        form = AuthenticationForm()
        error = None

    return render(request, 'core/login.html', {
        'form': form,
        'error': error
    })

def register_view(request):
    """
    Gestiona el registro de nuevos usuarios:
    - Si ya está autenticado, lo redirige al dashboard.
    - Con GET muestra el formulario de UserCreationForm.
    - Con POST valida y crea el usuario, lo autentica y redirige al dashboard.
    """
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()

    return render(request, 'core/register.html', {
        'form': form
    })

@login_required
def dashboard(request):
    """
    Panel principal visible solo si el usuario ha iniciado sesión.
    """
    return render(request, 'core/dashboard.html')

def logout_view(request):
    """
    Cierra la sesión del usuario y redirige a la landing.
    """
    logout(request)
    return redirect('landing')
