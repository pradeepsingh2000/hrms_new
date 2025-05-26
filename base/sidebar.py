from django.urls import reverse
from django.utils.translation import gettext_lazy as trans

MENU = trans("Approvals")
IMG_SRC = "images/ui/approval.svg"

SUBMENUS = [
    {
        "menu": trans("Leave"),
        "redirect": "/leave/user-request-view/",
    },
     {
        "menu": trans("Attendance"),
        "redirect": "/attendance/dashboard",
    },
    {
        "menu": trans("Shift"),
        "redirect": "/employee/shift-request-view/",
    },
     {
        "menu": trans("Overtime"),
        "redirect": "/attendance/dashboard",
    },
    {
        "menu": trans("Week Off"),
        "redirect": "/leave/user-request-view/",
    },
     {
        "menu": trans("Payroll"),
        "redirect": "/payroll/view-payroll-dashboard/",
    },
     {
        "menu": trans("Declaration"),
        "redirect": "/payroll/view-payroll-dashboard/",
    },
      {
        "menu": trans("Salary Revision"),
        "redirect": "#",  # You'll need to add the correct URL when available
    },
    {
        "menu": trans("Claim"),
        "redirect": "/leave/leave-dashboard",
    },
    {
        "menu": trans("Expense"),
        "redirect": "payroll/view-reimbursement/",
    },
    {
        "menu": trans("Assets"),
        "redirect": "/asset/asset-request-allocation-view/",
    }
    
] 