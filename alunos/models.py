from django.db import models

class Estado(models.Model):
    nome = models.CharField(max_length=50)
    sigla = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.nome} ({self.sigla})"
    
class Cidade(models.Model):
    nome = models.CharField(max_length=50)
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT)

    def __str__(self):
        return F"{self.nome} ({self.estado.sigla})"
    
class Pessoa(models.Model):
    nome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=11)
    email = models.EmailField(max_length=100)
    nasc = models.DateField
    cidade = models.ForeignKey(Cidade, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"
