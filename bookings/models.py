from django.db import models
from django.conf import settings
from grounds.models import Ground
from django.core.exceptions import ValidationError
from django.utils import timezone

class Booking(models.Model):
    ground = models.ForeignKey(Ground, on_delete=models.CASCADE, related_name='bookings')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='bookings')
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date', 'start_time']
        indexes = [
            models.Index(fields=['ground', 'date', 'start_time']),
        ]

    def clean(self):
        # Basic validation: start < end
        if self.start_time >= self.end_time:
            raise ValidationError("Start time must be before end time.")
        # Prevent booking in the past (date/time)
        dt_start = timezone.datetime.combine(self.date, self.start_time)
        if timezone.is_aware(dt_start):
            dt_start = timezone.make_naive(dt_start)
        if dt_start < timezone.localtime().replace(tzinfo=None):
            raise ValidationError("Cannot create bookings in the past.")

        # Conflict check: ensure no overlapping booking for same ground
        overlapping = Booking.objects.filter(
            ground=self.ground,
            date=self.date,
        ).exclude(pk=self.pk).filter(
            start_time__lt=self.end_time,
            end_time__gt=self.start_time
        )
        if overlapping.exists():
            raise ValidationError("This time slot is already booked for this ground.")

    def save(self, *args, **kwargs):
        self.full_clean()  # run clean() before saving
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} — {self.ground.name} on {self.date} from {self.start_time} to {self.end_time}"
