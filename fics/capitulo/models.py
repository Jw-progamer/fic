from django.db import models

# Create your models here
class Capitulo(models.Model):
    indice = models.IntegerField()
    titulo = models.CharField(max_length=100)
    texto = models.TextField()

    def __str__(self):
        return self.titulo
    