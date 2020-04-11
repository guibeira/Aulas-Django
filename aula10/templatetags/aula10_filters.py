from django import template
from django.template.defaultfilters import stringfilter

from aula8.models import Pet

register = template.Library()


@register.filter
@stringfilter
def swap(value):
    return value.swapcase()


@register.filter
def check_user(user):
    if user.is_authenticated:
        return f"<h1>Bem vindo {user}</h1>"
    return "<h1>vc não é bem vindo</h1>"


@register.filter
@stringfilter
def bold(value):
    return f"<b>{value}</b>"


@register.simple_tag
def pega_pet_pelo_nome(pet_name):
    pet = Pet.objects.get(nome=pet_name)
    return pet
