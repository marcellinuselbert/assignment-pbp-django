from django.test import TestCase

from katalog.models import CatalogItem

class TestModels(TestCase):

    def setUp(self):
        CatalogItem.objects.create(item_name="Kacang",item_price=2000,item_stock=2,description="ini kacang",rating=5,item_url="https://google.com")

    def test_catalog_models(self):
        kacang = CatalogItem.objects.get(item_name="Kacang")
        self.assertEqual(kacang.item_name, "Kacang")
    