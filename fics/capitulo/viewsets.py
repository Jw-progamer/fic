from rest_framework import viewsets
from .serializers import CapituloSerializer
from .models import Capitulo

class CapituloViewSet(viewsets.ModelViewSet):
    queryset = Capitulo.objects.all()
    serializer_class = CapituloSerializer
    # queryset = Capitulo.objects.filter(historia="")