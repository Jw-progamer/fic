from rest_framework import viewsets
from .serializers import CategoriaSerializer
from .models import Categoria

class CategoriaVieSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer