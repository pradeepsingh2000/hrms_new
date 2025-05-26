from django.urls import reverse
from django.utils.translation import gettext_lazy as trans

MENU = trans("Expense")
IMG_SRC = "images/ui/wallet-outline.svg"

SUBMENUS = [
    {
        "menu": trans("Dashboard"),
        "redirect": "#",
    },
    {
        "menu": trans("Category"),
        "redirect": "#",
    },
    {
        "menu": trans("Create Expense"),
        "redirect": "#",
    },
   
   
] 