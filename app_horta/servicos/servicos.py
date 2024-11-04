from ..models import Horta, SolicitacaoAcesso


def enviar_solicitacao(horta, usuario_solicitante):
    if horta.participantes.filter(id=usuario_solicitante.id).exists():
        return "Usuário já è participante"
    if SolicitacaoAcesso.objects.filter(horta=horta, usuario_solicitante=usuario_solicitante, aprovado=None).exists():
        return "Já existe uma solicitação pendete"
    
    solitacao = SolicitacaoAcesso(horta=horta,usuario_solicitante=usuario_solicitante)
    solitacao.save()
    return "Solicitação enviada com sucesso"

def aprovar_solicitacao(solicitacao_id):
    solicitacao = SolicitacaoAcesso.objects.get(id=solicitacao_id)
    if solicitacao.aprovado is not None:
        return "Solicitação já foi processada."
    solicitacao.aprovado = True
    solicitacao.save()
    solicitacao.horta.participantes.add(solicitacao.usuario_solicitante)
    return "Solicitação aprovada com sucesso."

def rejeitar_solicitacao(solicitacao_id):
    solicitacao = SolicitacaoAcesso.objects.get(id=solicitacao_id)
    if solicitacao.aprovado is not None:
        return "Solicitação já foi processada."
    solicitacao.aprovado = False
    solicitacao.save()
    return "Solicitação rejeitada com sucesso."



