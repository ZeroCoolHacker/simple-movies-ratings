from django.urls import path, include
from .views import MoviesList, MovieDetail


app_name = 'movies'

urlpatterns = [
    path('', MoviesList.as_view(), name='list'),
    path('<int:pk>', MovieDetail.as_view(), name='detail'),
]