# tests/test_views.py

from django.test import TestCase
from django.test_urls import reverse   # ✅ FIXED IMPORT

class HomeViewTest(TestCase):

    def test_home_status_code(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_home_template_used(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "home.html")