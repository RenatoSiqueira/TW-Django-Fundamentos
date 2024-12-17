from django.urls import path
from .views import cadastro_cliente, horario_atual

urlpatterns = [
    path('horario', horario_atual, name='horario_atual'),
    path('cadastro', cadastro_cliente, name='cadastro_cliente')
]
