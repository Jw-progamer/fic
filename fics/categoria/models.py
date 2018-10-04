from django.db import models

# Create your models here.
# class TipoCategoria(models.Model):
#   nome =  models.CharField(max_length=50)

#   def __str__(self):
#       return self.nome

# class Categoria(models.Model):
#   nome = models.CharField(max_length=50)
#   imagem = models.ImageField(upload_to=None, height_field=100, width_field=500, max_length=200)
#   tipo = models.ForeignKey("TipoCategoria", verbose_name="tipo", on_delete = models.SET_NULL)

#   def __str__(self):
#       return self.nome


class TipoCategoria(models.Model):
  nome = models.CharField(max_length=50)

  def __str__(self):
      return self.nome

class Categoria(models.Model):
  nome_categoria = models.CharField(max_length=50)
  imagem = models.ImageField(upload_to=None, height_field=100, width_field=500, max_length=200)
  tipo_categoria = models.ForeignKey(TipoCategoria, on_delete=models.CASCADE)

  def __str__(self):
      return self.nome_categoria
  
      
  
  
    
