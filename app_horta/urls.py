from django.urls import path
from app_horta.views import criar_horta, minha_horta, inserir_cultura, excluir_cultura, show_hortas, ingressar_horta, processar_solicitacao, horta_admin, criar_tarefa

urlpatterns = [
    path('horta/', minha_horta, name='minha_horta'),
    path('horta/criar', criar_horta, name='criar_horta'),
    path('horta/inserir/', inserir_cultura, name='inserir_cultura'),
    path('horta/excluir/<int:pk>', excluir_cultura, name='excluir_cultura'),
    path('horta/comunitarias', show_hortas, name='show_hortas'),
    path('horta/admin', horta_admin, name='admin'),
    path('horta/ingressar/<int:horta_id>/', ingressar_horta, name='ingressar_horta'),
    path('solicitacao/<int:solicitacao_id>/<str:acao>/', processar_solicitacao, name='processar_solicitacao'),
    path('horta/criar_tarefa/>', criar_tarefa, name='criar_tarefa'),
]