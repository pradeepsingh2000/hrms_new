from django.urls import path
from expense import views

urlpatterns = [
    path("expense-tab/<int:employee_id>/", views.expense_tab, name="expense-tab"),
    path("dashboard/", views.expense_dashboard, name="expense-dashboard"),
    path("my-expenses/", views.my_expenses, name="my-expenses"),
    path("team-expenses/", views.team_expenses, name="team-expenses"),
    path("reports/", views.expense_reports, name="expense-reports"),
    path("settings/", views.expense_settings, name="expense-settings"),
    # path("expense-list/", views.expense_list, name="expense-list"),
    # path("expense-create/", views.expense_create, name="expense-create"),
    # path("expense-update/<int:expense_id>/", views.expense_update, name="expense-update"),
    # path("expense-delete/<int:expense_id>/", views.expense_delete, name="expense-delete"),
] 