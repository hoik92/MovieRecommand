from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Genre, Movie, Score

# Create your views here.

def list(request):
    return render(request, 'movies/list.html')