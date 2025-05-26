from django.urls import reverse
from django.utils.translation import gettext_lazy as trans

MENU = trans("Approvals")
IMG_SRC = "images/ui/approval.svg"

SUBMENUS = [
    {
        "menu": trans("Leave"),
        "redirect": "/leave/request-view/",
    },
     {
        "menu": trans("Attendance"),
        "redirect": "/attendance/attendance-view",
    },
    {
        "menu": trans("Shift"),
        "redirect": "/employee/shift-request-view/",
    },
     {
        "menu": trans("Overtime"),
        "redirect": "/leave/overtime",
    },
    {
        "menu": trans("Week Off"),
        "redirect": "/leave/week-off/",
    },
     {
        "menu": trans("Payroll"),
        "redirect": "/leave/payrole/",
    },
     {
        "menu": trans("Declaration"),
        "redirect": "/leave/declaration/",
    },
      {
        "menu": trans("Salary Revision"),
        "redirect": "/leave/salary-revision/"  # You'll need to add the correct URL when available
    },
    {
        "menu": trans("Claim"),
        "redirect": "/leave/claim/",
    },
    {
        "menu": trans("Expense"),
        "redirect": "/leave/expense/",
    },
    {
        "menu": trans("Assets"),
        "redirect": "/asset/asset-request-allocation-view/",
    }
    
] 