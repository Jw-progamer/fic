from django.db import models

class Autor(models.Model):
    nome = models.CharField(max_length=255)
    usuario = models.CharField(max_length=255)
    idade = models.IntegerField()
    data_inscricao = models.DateField( auto_now_add=True, editable=False)
    descricao = models.TextField(max_length=255)

    def __str__(self):
        return self.usuario

    
    
    

