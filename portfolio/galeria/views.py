from django.shortcuts import render
from django.conf import settings
from .models import Proyecto

# Create your views here.


def portfolio(request):
    projects = Proyecto.objects.all()

    return render(request, 'galeria/portfolio.html', {'settings': settings.FECHAS, 'projects': projects})
