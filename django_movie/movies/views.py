from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Movie
# Create your views here.

class MoviesView(ListView):
    """Список фильмов"""

    model = Movie
    queryset = Movie.objects.filter(draft=False)


class MovieDetailView(DetailView):
    """Полное описание фильма"""
    model = Movie
    slug_field = "url"
