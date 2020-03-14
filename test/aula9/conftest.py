import pytest
from django.urls import reverse


@pytest.fixture
def response_aula9_view(client):
    return client.get(reverse("aula9"))