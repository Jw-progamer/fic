from rest_framework import serializers
from .models import Categoria

class CategoriaSerializer(serializers.Serializer):
    class Meta:
        model = Categoria
        fields = ('id','nome_categoria','imagem','tipo_categoria')