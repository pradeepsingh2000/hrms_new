from django.db import models
from django.utils import timezone

class Expense(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    CATEGORY_CHOICES = [
        ('travel', 'Travel'),
        ('supplies', 'Supplies'),
        ('technology', 'Technology'),
        ('meals', 'Meals'),
        ('training', 'Training'),
        ('other', 'Other'),
    ]

    description = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(default=timezone.now)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.description} - ${self.amount} ({self.status})"
