from django.test import TestCase
from django.urls import reverse

# Create your tests here.


class TestLogoutView(TestCase):
    def setUp(self):
        self.url = reverse("logout")

    def test_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)

    def test_redirect(self):
        response = self.client.get(self.url)
        self.assertRedirects(response, reverse("login"))
