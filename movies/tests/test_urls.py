from django.test import SimpleTestCase
from django.urls import reverse, resolve
from movies.views import MoviesList, MovieDetail


class TestUrls(SimpleTestCase):

    def test_movies_list_url_is_resolved(self):
        url = reverse('movies:list')
        self.assertEqual(resolve(url).func.view_class, MoviesList)

    def test_movie_detail_url_is_resolved(self):
        url = reverse('movies:detail', args=[1])
        self.assertEqual(resolve(url).func.view_class, MovieDetail)