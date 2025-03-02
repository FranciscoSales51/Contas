from django.core.management.base import BaseCommand
from cadastro_contas.models import Categoria

class Command(BaseCommand):
    help = 'Popula o banco de dados com categorias iniciais'

    def handle(self, *args, **kwargs):
        categorias = ['Cartões', 'Água', 'Luz', 'Internet','Plano de Saúde', 'Gás','Terreno','Rastreador Moto','Manutenção de Moto','Outros' ]
        for nome in categorias:
            Categoria.objects.get_or_create(nome=nome)
        self.stdout.write(self.style.SUCCESS('Categorias populadas com sucesso!'))
