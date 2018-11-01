from rest_framework import viewsets
from .serializers import HistoriaSerializer
from .models import Historia
from autor.models import Autor
from rest_framework.decorators import list_route, action
from rest_framework.response import Response

class HistoriaViewSet(viewsets.ModelViewSet):
    queryset = Historia.objects.all()
    serializer_class = HistoriaSerializer

    @action(detail=False, methods=['GET'], url_path='getautor/(?P<usuario>[^/.]+)')
    def get_autor(self, request, usuario=None):
        autor = Autor.objects.filter(usuario = usuario).first()
        if not autor:
            return Response({'detail': 'Not Found!'}, 404)

        history = Historia.objects.filter(autor=autor)
        return Response(data = {'historias': self.serializer_class(history, many=True).data})