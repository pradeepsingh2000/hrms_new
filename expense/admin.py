from django.contrib import admin
from expense.models import Expense, ExpenseType

# Register your models here.
admin.site.register(Expense)
admin.site.register(ExpenseType)
