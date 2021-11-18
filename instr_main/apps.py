from django.apps import AppConfig


class InstrMainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'instr_main'
    def ready(self):
        import instr_main.signals
