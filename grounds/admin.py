from django.contrib import admin
from .models import Ground

@admin.register(Ground)
class GroundAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'price_per_hour', 'manager', 'created_at')
    search_fields = ('name', 'location', 'manager__username')
