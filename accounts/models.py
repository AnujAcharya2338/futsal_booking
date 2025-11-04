
# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('manager', 'Manager'),
        ('customer', 'Customer'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='customer')

    def is_manager(self):
        return self.role == 'manager'

    def is_customer(self):
        return self.role == 'customer'

    def __str__(self):
        return f"{self.username} ({self.role})"
class ManagerProfile(models.Model):
    user = models.OneToOneField('CustomUser', on_delete=models.CASCADE, related_name='manager_profile')
    phone = models.CharField(max_length=32, blank=True, null=True)
    futsal_name = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return f"Profile for {self.user.username}"
