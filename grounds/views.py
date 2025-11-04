from django.shortcuts import render

def grounds_list(request):
    return render(request, 'grounds.html')
