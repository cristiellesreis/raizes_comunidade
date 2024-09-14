from django.shortcuts import render
from .models import Atividade
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from app_clima.views import  clima
from app_clima.forms import CidadesForms

def home(request):
    if request.method == 'POST':
        form = CidadesForms(request.POST)
        if form.is_valid():
            cidade = form.cleaned_data['cidade']
    else:
        cidade = 'santos'
        form = CidadesForms(initial={'cidade': cidade})
    
    dados_clima = clima(cidade)
    
    contexto = {
        'clima': dados_clima,
        'form': form
    }
    
    return render(request, "home.html", contexto)

@login_required(login_url="/login/login/")
def atividades(request):
    lista_atividades = {}
    
    if request.method == 'POST':
        atividade = request.POST.get("atividade")
        dt_atividade = request.POST.get("dt_atividade")
        usuario_id = request.user.username
        nova_atividade = Atividade(atividade=atividade, dt_atividadedb=dt_atividade ,usuario_id=usuario_id )
        nova_atividade.save()
                    
    lista_atividades["atividades"] = Atividade.objects.all().order_by('-dt_atividadedb')[:10]
    
    return render(request, "atividades/atividade.html", lista_atividades)