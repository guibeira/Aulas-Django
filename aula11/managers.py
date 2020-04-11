from django.db.models import Manager


class CustomPostManager(Manager):
    def total_publicados(self):
        return self.all().count()

    def get_queryset(self):
        return super().get_queryset().filter(deletado=False)


class TecPostManager(CustomPostManager):
    def get_queryset(self):
        return super().get_queryset().filter(categoria__nome="tecnologia")
