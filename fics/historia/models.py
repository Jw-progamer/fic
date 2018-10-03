from django.db import models

# Create your models here.
class Historia(models.Model):

    FAIXA_ETARIA = (
        ('LIVRE', 0),
        ('INFANT', 3),
        ('CHILD',5),
        ('YOUNG', 10),
        ('TEEN', 13),
        ('ADULT',16),
        ('FORIBEN',18)
    )

    titulo = models.CharField(max_length=100)
    autor = models.ForeignKey("Autor", verbose_name=("autor"), on_delete=models.CASCADE)
    descricao = models.TextField()
    restricao_etaria = models.IntegerField(verbose_name="Restrição de Idade",choices=FAIXA_ETARIA)
    data_publicacao = models.DateField(auto_now=False, auto_now_add=True)
    categorias = models.ManyToManyField("Categoria", verbose_name=("categorias"))
    generos = models.ManyToManyField("Genero", verbose_name=(""))
    completa = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo

class Genero(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
        
    
