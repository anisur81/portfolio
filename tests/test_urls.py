from django.tests import SimpleTestCase
from django.urls import reverse, resolve
from tests.views import home   # ✅ FIXED

class TestUrls(SimpleTestCase):

    def test_home_url_resolves(self):
        url = reverse("home")
        self.assertEqual(resolve(url).func, home)