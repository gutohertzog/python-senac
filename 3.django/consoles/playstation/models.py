from django.db import models

class Modelo(models.Model):
    nome = models.CharField(max_length=100)
    sigla = models.CharField(max_length=100)
    descricao = models.CharField(max_length=200)
    data_lanc = models.DateField()
    foto = models.ImageField(upload_to='imagens/%Y/%m/%d/')
    link = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
