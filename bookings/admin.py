from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('ground', 'user', 'date', 'start_time', 'end_time', 'created_at')
    list_filter = ('ground', 'date')
