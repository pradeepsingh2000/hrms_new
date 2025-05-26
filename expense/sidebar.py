from django.urls import reverse
from django.utils.translation import gettext_lazy as trans

MENU = trans("Expense")
IMG_SRC = "images/ui/wallet-outline.svg"

SUBMENUS = [
    {
        "menu": trans("Dashboard"),
        "redirect": "/report/dashboard",
    },
    {
        "menu": trans("Category"),
        "redirect": "/report/category",
    },
    {
        "menu": trans("Create Expense"),
        "redirect": "/report/create-category",
    },
   
   
] 