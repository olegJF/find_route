from django.shortcuts import render
from routes.forms import RouteForm


def home(request):
    form = RouteForm()
    return render(request, 'routes/home.html', {'form': form})
