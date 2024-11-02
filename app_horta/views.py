from django.shortcuts import render, redirect, get_object_or_404
from .models import Horta, Cultura, SolicitacaoAcesso
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User
from .servicos.servicos import enviar_solicitacao, aprovar_solicitacao, rejeitar_solicitacao
from django.contrib import messages



@login_required(login_url="/login/login/")
def minha_horta(request):
    try:
        horta_do_usuario = Horta.objects.filter(participantes=request.user).first() or Horta.objects.filter(usuario=request.user).first()
        if not horta_do_usuario:
            return render(request, 'horta/horta.html')

        horta_id = horta_do_usuario.id
        membros = horta_do_usuario.participantes.all()
        lista_culturas = Cultura.objects.filter(horta_id=horta_id)

        return render(request, 'horta/horta.html', {
            'horta': horta_do_usuario,
            'culturas': lista_culturas,
            'membros': membros,
        })
    except Exception as e:
        print(f"Erro ao carregar horta: {e}")
        return render(request, 'horta/horta.html', {'error': 'Ocorreu um erro ao carregar a horta.'})

       
    
@login_required
def criar_horta(request):
    if request.method == "POST":
       nome = request.POST.get('nome')
       descricao = request.POST.get('descricao')
       comunitaria = False
       
       if request.user.groups.filter(name="Líder Comunitário").exists():
           comunitaria = True
       
       nova_horta = Horta(usuario= request.user, nome=nome,descricao=descricao, comunitaria=comunitaria)
       nova_horta.save()
       return redirect("minha_horta")
    else:
        return render(request, 'horta/criar_horta.html')


@login_required
def show_hortas(request):
    lista_hortas = Horta.objects.filter(comunitaria=True)
    
    if lista_hortas.exists():
        return render(request, 'horta/hortas_comunitarias.html', {'lista_hortas': lista_hortas})
    else:
        return render(request, 'horta/hortas_comunitarias.html', {'error_message': 'Não há hortas comunitárias Disponíveis'})

def ingressar_horta(request, horta_id):
    horta = get_object_or_404(Horta, id=horta_id)
    resultado = enviar_solicitacao(horta, request.user)
    return redirect('minha_horta') 

def processar_solicitacao(request, solicitacao_id, acao):
    if acao == 'aprovar':
        resultado = aprovar_solicitacao(solicitacao_id)
    elif acao == 'rejeitar':
        resultado = rejeitar_solicitacao(solicitacao_id)
    else:
        resultado = "Ação inválida."
    messages.success(request, resultado)
    return redirect('minha_horta')


@login_required
def inserir_cultura(request):
    
    if request.method == 'POST':
        horta_usuario = Horta.objects.filter(participantes=request.user).first() or Horta.objects.filter(usuario=request.user).first()
        horta_id = horta_usuario.id

        nome = request.POST.get('nome_cultura')
        tipo = request.POST.get('tipo_cultura')
        descricao = request.POST.get('desc_cultura')
        
        nova_cultura = Cultura(horta_id= horta_id, name=nome, type=tipo, desc=descricao)

        nova_cultura.save()
        
        return redirect('minha_horta')
    
    return render(request, "horta/horta.html")

@login_required
def excluir_cultura(request, pk):
    if request.method == 'POST':
        cultura = get_object_or_404(Cultura, pk=pk)
        cultura.delete()
        return redirect('minha_horta')
    else:
        return redirect('minha_horta')

        
@login_required
def horta_admin(request):
    solicitacoes_pendentes = []
    solicitacoes_pendentes = SolicitacaoAcesso.objects.filter(
        horta = Horta.objects.filter(usuario=request.user).first(),
        aprovado=None
    )
    return render(request, "horta/admin.html", {'solicitacoes': solicitacoes_pendentes})
    