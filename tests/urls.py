# your_app/tests/test_urls.py

from django.test import SimpleTestCase
from django.urls import reverse, resolve
from your_app.views import home

class UrlTest(SimpleTestCase):

    def test_home_url_resolves(self):
        url = reverse("home")
        self.assertEqual(resolve(url).func, home)