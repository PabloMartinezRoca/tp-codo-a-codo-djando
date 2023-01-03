from django.shortcuts import render
from django.conf import settings

# Create your views here.


def home(request):
    return render(request, 'core/home.html', settings.FECHAS)


def about(request):
    return render(request, 'core/about.html', settings.FECHAS)


def contacto(request):
    return render(request, 'core/contacto.html', settings.FECHAS)
