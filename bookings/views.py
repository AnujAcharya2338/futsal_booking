from django.shortcuts import render

def bookings_list(request):
    return render(request, 'bookings.html')
