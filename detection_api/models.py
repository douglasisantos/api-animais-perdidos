from django.db import models
from django.utils import timezone
class AnimalPerdido(models.Model):
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    raca = models.CharField(max_length=100)
    descricao_objetos = models.CharField(max_length=100, default='Descrição não fornecida')  # Novo campo para a descrição dos objetos detectados
    foto = models.ImageField(upload_to='animais/')
    data_criacao = models.DateTimeField(default=timezone.now)
    endereco = models.CharField(max_length=100, default='')
    def __str__(self):
        return self.nome
