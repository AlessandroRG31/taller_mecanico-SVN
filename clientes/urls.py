from django.urls import path
from .views import ClienteListView, ClienteCreateView, ClienteAutocomplete

app_name = 'clientes'

urlpatterns = [
    path('', ClienteListView.as_view(), name='list'),
    path('nuevo/', ClienteCreateView.as_view(), name='create'),
    path('autocomplete/', ClienteAutocomplete.as_view(), name='cliente-autocomplete'),
]
