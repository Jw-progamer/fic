from rest_framework import serializers
from .models import Capitulo

class CapituloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Capitulo
        fields = ('id','indice','titulo','texto','historia')