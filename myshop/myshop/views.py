# myshop/views.py

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')  # Create a home.html template
