# tests/test_urls.py

from django.test import SimpleTestCase
from django.urls import reverse, resolve
from tests.test_views import home   # adjust if your view name differs

class TestUrls(SimpleTestCase):

    def test_home_url_resolves(self):
        url = reverse("home")
        self.assertEqual(resolve(url).func, home)