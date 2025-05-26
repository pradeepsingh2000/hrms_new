from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.decorators import login_required
from horilla.decorators import permission_required, owner_can_enter
from employee.models import Employee
from expense.models import Expense, ExpenseType

@login_required
@owner_can_enter("expense.view_expense", Employee)
def expense_tab(request, employee_id):
    """
    View for the expense tab in employee profile
    """
    
    context = {
        "expenses": ["pradeep"],
        "employee": ["negi"],
    }
    return render(request, "expense/tab/expense_tab.html", context)

# @login_required
# @permission_required("expense.view_expense")
# def expense_list(request):
#     """
#     View for listing all expenses
#     """
#     expenses = Expense.objects.all()
#     context = {
#         "expenses": expenses,
#     }
#     return render(request, "expense/expense_list.html", context)

# @login_required
# @permission_required("expense.add_expense")
# def expense_create(request):
#     """
#     View for creating a new expense
#     """
#     if request.method == "POST":
#         # Add your form handling logic here
#         messages.success(request, _("Expense created successfully"))
#         return redirect("expense-list")
#     return render(request, "expense/expense_create.html")

# @login_required
# @permission_required("expense.change_expense")
# def expense_update(request, expense_id):
#     """
#     View for updating an expense
#     """
#     expense = Expense.objects.get(id=expense_id)
#     if request.method == "POST":
#         # Add your form handling logic here
#         messages.success(request, _("Expense updated successfully"))
#         return redirect("expense-list")
#     context = {
#         "expense": expense,
#     }
#     return render(request, "expense/expense_update.html", context)

# @login_required
# @permission_required("expense.delete_expense")
# def expense_delete(request, expense_id):
#     """
#     View for deleting an expense
#     """
#     expense = Expense.objects.get(id=expense_id)
#     expense.delete()
#     messages.success(request, _("Expense deleted successfully"))
#     return redirect("expense-list")

@login_required
def expense_dashboard(request):
    """View for expense dashboard"""
    context = {}
    return render(request, "expense/dashboard.html", context)

@login_required
def my_expenses(request):
    """View for user's own expenses"""
    context = {}
    return render(request, "expense/my_expenses.html", context)

@login_required
def team_expenses(request):
    """View for team expenses"""
    context = {}
    return render(request, "expense/team_expenses.html", context)

@login_required
def expense_reports(request):
    """View for expense reports"""
    context = {}
    return render(request, "expense/reports.html", context)

@login_required
def expense_settings(request):
    """View for expense settings"""
    context = {}
    return render(request, "expense/settings.html", context)
