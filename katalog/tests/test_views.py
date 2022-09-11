from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):

    def test_show_catalog_resolved(self):
  
        
        # this code give strange error??
        
        client = Client()
        response = client.get(reverse("katalog:katalog"))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'katalog.html')
        
