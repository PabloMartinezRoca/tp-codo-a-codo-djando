from django.shortcuts import render
from django.conf import settings
# Create your views here.


def portfolio(request):
    return render(request, 'galeria/portfolio.html', settings.FECHAS)
