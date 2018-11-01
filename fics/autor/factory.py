from .models import Autor
import factory
class FactoryHistoria(factory.django.DjangoModelFactory):
    class Meta:
        model = Autor
    nome = factory.Faker('name',locale='pt-br')
    usario = factory.Faker('name', locale='pt-br')
    idade = 18
    data_inscricao = factory.Faker('date')
    descricao = "lorem ipslun et donet all it"