from django.urls import path
from . import views

urlpatterns = [
    path('', views.bookings_list, name='bookings_list'),
]
