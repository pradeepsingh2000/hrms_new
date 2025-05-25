from django.urls import reverse
from django.utils.translation import gettext_lazy as trans

MENU = trans("Reports")
IMG_SRC = "images/ui/report.svg"
REDIRECT = reverse("newReport:view_report")
SUBMENUS = [] 