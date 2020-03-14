from django.urls import reverse
from unittest import mock


@mock.patch("aula10.context_processors.total_pets")
def test_mostra_arquivo_estatico(mock_total_pet ,client):
    mock_total_pet.return_value = {"total_pet": 0}
    response = client.get(reverse("aula10"))
    assert response.status_code == 200
