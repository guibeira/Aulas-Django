from django.apps import AppConfig


class Aula11Config(AppConfig):
    name = 'aula11'

    def ready(self):
        import aula11.signals
