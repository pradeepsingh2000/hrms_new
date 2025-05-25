from django.apps import AppConfig


class NewReportConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "newReport"

    def ready(self):
        from django.urls import include, path
        from horilla.horilla_settings import APPS
        from horilla.urls import urlpatterns

        APPS.append("newReport")
        super().ready()
