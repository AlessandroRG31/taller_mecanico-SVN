from django.urls import path
from .views import landing, login_view, register_view, dashboard, logout_view

urlpatterns = [
    path('',           landing,       name='landing'),   # GET  /
    path('login/',     login_view,    name='login'),     # GET/POST /login/
    path('register/',  register_view, name='register'),  # GET/POST /register/
    path('dashboard/', dashboard,     name='dashboard'), # GET  /dashboard/
    path('logout/',    logout_view,   name='logout'),    # GET  /logout/
]
