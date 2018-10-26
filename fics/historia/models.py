from django.db import models
from categoria.models import Categoria
from autor.models import Autor
# Create your models here.


class Genero(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Historia(models.Model):

    FAIXA_ETARIA = (
        (0,'LIVRE'),
        (3,'INFANT'),
        (5,'CHILD'),
        (10,'YOUNG'),
        (13,'TEEN'),
        (16,'ADULT'),
        (18,'FORIBEN')
    )

    titulo = models.CharField(max_length=100)
    autor = models.ForeignKey(Autor, verbose_name=("autor"), on_delete=models.CASCADE)
    descricao = models.TextField()
    restricao_etaria = models.IntegerField(verbose_name="Restrição de Idade",choices=FAIXA_ETARIA)
    data_publicacao = models.DateField(auto_now=False, auto_now_add=True)
    categorias = models.ManyToManyField(Categoria, verbose_name=("categorias"))
    generos = models.ManyToManyField(Genero, verbose_name=(""))
    completa = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo
        
    
