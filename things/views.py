from django.shortcuts import render

def home(request):
    """Display the application's start/home screen."""

    return render(request, 'home.html')