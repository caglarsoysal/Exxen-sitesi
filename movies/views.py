from django.shortcuts import render
from .models import *
# Create your views here.
def index (request):
    filmler = Movie.objects.all()
    context = {
        'filmler':filmler
    }
    return render(request, 'exxen.html', context)