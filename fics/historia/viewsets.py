from rest_framework import viewsets
from .serializers import HistoriaSerializer
from .models import Historia

class HistoriaViewSet(viewsets.ModelViewSet):
    queryset = Historia.objects.all()
    serializer_class = HistoriaSerializer