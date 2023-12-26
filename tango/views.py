from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def home(request):
    return render(request, 'tango/home.html')


def contact(request):
    return render(request, 'tango/contact.html')


def about(request):
    return render(request, 'tango/about.html')

