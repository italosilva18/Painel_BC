from django.db import models
from django.contrib.auth.models import User

class Funcao(models.Model):
    nome = models.CharField(max_length=100)

class Funcionario(User):
    idade = models.IntegerField()
    funcao = models.ForeignKey(Funcao, on_delete=models.CASCADE)

class Equipamento(models.Model):
    nome = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    validade = models.DateField()
    informacoes = models.TextField()
    observacao = models.TextField()

class InspecaoEquipamento(models.Model):
    equipamento = models.ForeignKey(Equipamento, on_delete=models.CASCADE)
    inspecao = models.TextField()
    observacao = models.TextField()
    data_inspecao = models.DateField(auto_now=True)
    
class RegistroEvento(models.Model):
    hora_inicial_evento = models.DateTimeField()
    hora_final_evento = models.DateTimeField()
    ronda_interna = models.BooleanField()
    ronda_externa = models.BooleanField()
    visitas = models.TextField()
    manobras = models.TextField()
    imagens_videos = models.FileField(upload_to='registro/uploads/%Y-%m-%d')
    

class RegistroAtividade(models.Model):
    DEMANDA_CHOICES = [
        ('sim', 'Sim'),
        ('nao', 'Não'),
    ]
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    numero_ordem_servico = models.IntegerField()
    data_registro = models.DateField()
    turno_atual = models.CharField(max_length=100)
    evento = models.ManyToManyField(RegistroEvento)
    inspecoes_equipamentos = models.ManyToManyField(InspecaoEquipamento)
    evento_automatico = models.BooleanField(default=False)
    demanda = models.CharField(max_length=3, choices=DEMANDA_CHOICES, default='nao')
    texto_demanda = models.TextField(blank=True, null=True)
    



    
