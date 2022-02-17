from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView

from .models import Movie
from .forms import ReviewForm
# Create your views here.

class MoviesView(ListView):
    """Список фильмов"""

    model = Movie
    queryset = Movie.objects.filter(draft=False)


class MovieDetailView(DetailView):
    """Полное описание фильма"""
    model = Movie
    slug_field = "url"


class AddReview(View):
    """Отзывы"""
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)      # приостанавливает сохранение формы в базу
            form.movie = movie
            form.save()
        return redirect(movie.get_absolute_url())