from django.urls import path
from . import views

urlpatterns = [
    path('', views.grounds_list, name='grounds_list'),
]
