from django.urls import path
from .views import cadastro_contas, pagina_inicial

urlpatterns = [
    path('', pagina_inicial, name='pagina_inicial'),
    path('cadastro_contas/', cadastro_contas, name='cadastro_contas'),
]
