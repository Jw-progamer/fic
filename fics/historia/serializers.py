from rest_framework import serializers
from .models import Historia

class HistoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historia
        fields = ('id','titulo','autor','descricao','restricao_etaria','data_publicacao','categorias','generos','completa')