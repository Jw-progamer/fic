from django.db import models
from historia.models import Historia

# Create your models here
class Capitulo(models.Model):
    indice = models.IntegerField()
    titulo = models.CharField(max_length=100)
    texto = models.TextField()
    historia = models.ForeignKey(Historia, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
    