from django.db import models
from django.utils.translation import gettext_lazy as _
from base.models import HorillaModel
from employee.models import Employee

class ExpenseType(HorillaModel):
    """
    ExpenseType model
    """
    name = models.CharField(max_length=100, verbose_name=_("Name"))
    description = models.TextField(null=True, blank=True, verbose_name=_("Description"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Expense Type")
        verbose_name_plural = _("Expense Types")
        ordering = ["-id"]

class Expense(HorillaModel):
    """
    Expense model
    """
    STATUS_CHOICES = [
        ("pending", _("Pending")),
        ("approved", _("Approved")),
        ("rejected", _("Rejected")),
    ]

    employee = models.ForeignKey(
        Employee, 
        on_delete=models.PROTECT,
        related_name="expenses",
        verbose_name=_("Employee")
    )
    expense_type = models.ForeignKey(
        ExpenseType,
        on_delete=models.PROTECT,
        related_name="expenses",
        verbose_name=_("Expense Type")
    )
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name=_("Amount")
    )
    date = models.DateField(verbose_name=_("Date"))
    description = models.TextField(verbose_name=_("Description"))
    attachment = models.FileField(
        upload_to="expense_attachments/",
        null=True,
        blank=True,
        verbose_name=_("Attachment")
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending",
        verbose_name=_("Status")
    )
    approved_by = models.ForeignKey(
        Employee,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="approved_expenses",
        verbose_name=_("Approved By")
    )
    approved_date = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name=_("Approved Date")
    )
    rejection_reason = models.TextField(
        null=True,
        blank=True,
        verbose_name=_("Rejection Reason")
    )

    def __str__(self):
        return f"{self.employee} - {self.expense_type} - {self.amount}"

    class Meta:
        verbose_name = _("Expense")
        verbose_name_plural = _("Expenses")
        ordering = ["-date", "-id"]
