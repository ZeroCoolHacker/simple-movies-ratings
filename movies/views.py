from django.views.generic import ListView, DetailView
from .models import Movie

class MoviesList(ListView):
    template_name = 'movies/home.html'
    context_object_name = 'movies'
    model = Movie

class MovieDetail(DetailView):
    template_name = 'movies/detail.html'
    context_object_name = 'movie'
    model = Movie