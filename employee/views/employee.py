from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Employee

@login_required
def investment_data(request, employee_id):
    """View for investment data"""
    employee = Employee.objects.get(id=employee_id)
    context = {
        "employee": employee,
    }
    return render(request, "tabs/investment_data.html", context)

@login_required
def id_proof_data(request, employee_id):
    """View for ID proof data"""
    employee = Employee.objects.get(id=employee_id)
    context = {
        "employee": employee,
    }
    return render(request, "tabs/id_proof_data.html", context) 