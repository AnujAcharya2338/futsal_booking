from django.db import models
from django.conf import settings

class Ground(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=255)
    price_per_hour = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='grounds/', blank=True, null=True)
    manager = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='grounds',
        limit_choices_to={'role': 'manager'}
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
