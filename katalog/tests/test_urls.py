from django.test import TestCase
from django.urls import reverse, resolve
from katalog.views import show_katalog

class TestUrls(TestCase):

    def test_katalog_url_is_resolved(self):
        url = reverse("katalog:katalog")
        self.assertEquals(resolve(url).func,show_katalog)