from django.test import TestCase
from autor.models import Autor
from django.urls import reverse_lazy
# Create your tests here.

class TestHistria(TestCase):
    # def setUp(self):
    def test_posso_fitrar_historias_por_autor(self):
       
        autor = Autor.
        
        params = {
            'pk': autor.pk
        }
        import ipdb; ipdb.set_trace()
        response =  self.client.get(reverse_lazy('historia'), params=params )
        print(response.content)
        self.assertEqual(response.status_code, 200)