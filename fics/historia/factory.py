from .models import Historia
from autor.models import Autor
import factory
class FactoryHistoria(factory.django.DjangoModelFactory):
    class Meta:
        model = Historia
    titulo = "Titulo de teste"
    autor = factory.SubFactory(Autor)
    descricao = 'Loren ipslun et donet al it'
    restricao_etaria = 5
    data_publicacao = factory.Faker('date')

