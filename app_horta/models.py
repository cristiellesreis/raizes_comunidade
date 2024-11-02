from django.db import models
from django.db import models
from django.contrib.auth.models import User

class Horta(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(null= False, max_length=50)
    descricao = models.CharField(max_length=150)
    comunitaria = models.BooleanField(default=False)
    participantes = models.ManyToManyField(User, related_name="hortas_comunitarias",blank=True)

    def __str__(self):
        return self.nome
    
class SolicitacaoAcesso(models.Model):
    horta = models.ForeignKey(Horta,on_delete=models.CASCADE)
    usuario_solicitante = models.ForeignKey(User, on_delete=models.CASCADE)
    data_solicitacao = models.DateTimeField(auto_now_add=True)
    aprovado = models.BooleanField(null=True, default=None)
    
    def __str__(self):
        return f"Solicitação de {self.usuario_solicitante} para {self.horta.nome}"
    
    
class Cultura(models.Model):
    horta = models.ForeignKey(Horta, on_delete=models.CASCADE)
    name = models.CharField(null= False, max_length=50)
    type = models.CharField(max_length=50)
    desc = models.CharField(max_length=150)
    
    def __str__(self):
        return f"{self.name} - {self.type} - {self.desc}"
    
class Plantio(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    cultura = models.ForeignKey(Cultura, on_delete=models.CASCADE)
    dt_plantio = models.DateField(null=False)
    ultima_atv = models.DateField(null=True)
    descricao_atv = models.CharField(max_length=150,null= True)
    

