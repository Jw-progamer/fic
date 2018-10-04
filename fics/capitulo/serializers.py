from rest_framework import serializers
from .models import Capitulo

class CapituloSerializer(serializers.Serializer):
    class Meta:
        model = Capitulo
        fields = ('id','indice','titulo','texto','historia')