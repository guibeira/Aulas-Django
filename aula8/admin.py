from django.contrib import admin

from .forms import PetForm
from .models import Pet


class PetAdmin(admin.ModelAdmin):
    fields = ("nome", "data_nascimento", "ativo")
    list_display = ("nome", "data_nascimento", "show_and_year", "ativo")
    list_filter = ("ativo",)
    search_fields = ("nome",)
    form = PetForm

    def show_and_year(self, obj):
        return f"{obj.nome} {obj.data_nascimento}"


admin.site.register(Pet, PetAdmin)
