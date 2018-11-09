from rest_framework import viewsets
from .serializers import CapituloSerializer
from .models import Capitulo
from historia.models import Historia
from rest_framework.decorators import list_route, action
from rest_framework.response import Response

class CapituloViewSet(viewsets.ModelViewSet):
    queryset = Capitulo.objects.all()
    serializer_class = CapituloSerializer
    
    @action(detail=False, methods=['GET'], url_path='getcapitulos/(?P<pk>[^/.]+)')
    def get_capitulos_historia(self, request, pk=None):
        historia = Historia.objects.filter(pk = pk).first()
        if not historia:
            return Response({'detail': 'Not Found!'}, 404)

        capitulos= Capitulo.objects.filter(historia=historia)
        return Response(data = {'capitulos': self.serializer_class(capitulos, many=True).data})