from django.test import TestCase
from django.urls import reverse
# Create your tests here.

class TestIndexView(TestCase):

    def setUp(self):
        self.url = reverse("aula9")

    def test_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_template(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "aula9/aula9.html")
        self.assertTemplateUsed(response, "base.html")

    def test_context(self):
        response = self.client.get(self.url)
        self.assertEqual("Guilherme", response.context["nome"])



