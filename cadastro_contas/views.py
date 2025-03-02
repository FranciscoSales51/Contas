from django.shortcuts import render, redirect
from .models import Conta, Categoria
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import datetime

@login_required
def cadastro_contas(request):
    if request.method == 'POST':
        categoria_id = request.POST.get('categoria')
        descricao = request.POST.get('descricao')
        valor = request.POST.get('valor')
        data_vencimento = request.POST.get('data_vencimento')
        categoria = Categoria.objects.get(id=categoria_id)
        Conta.objects.create(categoria=categoria, descricao=descricao, valor=valor, data_vencimento=data_vencimento)
        messages.success(request, 'Conta cadastrada com sucesso!')
        return redirect('cadastro_contas')
    
    categorias = Categoria.objects.all()
    contas = Conta.objects.all()
    total_contas = sum([conta.valor for conta in contas])
    agora = datetime.now()
    contexto = {
        'categorias': categorias,
        'contas': contas,
        'total_contas': total_contas,
        'data_hora_atual': agora.strftime("%d/%m/%Y %H:%M")
    }
    return render(request, 'cadastro_contas.html', contexto)

def pagina_inicial(request):
    return render(request, 'pagina_inicial.html')
