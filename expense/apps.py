from django.apps import AppConfig
from django.urls import include, path


class ExpenseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'expense'

    def ready(self):
        from horilla.horilla_settings import APPS
        from horilla.urls import urlpatterns

        APPS.append("expense")
        urlpatterns.append(
            path("expense/", include("expense.urls")),
        )
        super().ready()
