from django.apps import AppConfig


class GwmConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.gwm"

    def ready(self):
        import apps.gwm.signals
