from django.shortcuts import render, HttpResponse
import datetime

# Create your views here.

today = datetime.date.today()
year = today.year
context = {
    'year': year,
}


def home(request):
    return render(request, 'core/home.html', context)


def about(request):
    return render(request, 'core/about.html', context)


def portfolio(request):
    return render(request, 'core/portfolio.html', context)


def contacto(request):
    return render(request, 'core/contacto.html', context)
