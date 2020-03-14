from aula8.forms import PetForm
from datetime import date
import pytest


def test_pet_form():
    data = {
        "nome": "rex",
        "data_nascimento": date(2019, 1, 1)
    }
    form = PetForm(data=data)

    assert form.is_valid()


@pytest.mark.parametrize("name", ["Putinho", "pUtinho", "PUTINHO"])
def test_pet_invalid(name):
    data = {
        "nome": name,
        "data_nascimento": date(2019, 1, 1)
    }
    form = PetForm(data=data)

    assert form.is_valid() is False