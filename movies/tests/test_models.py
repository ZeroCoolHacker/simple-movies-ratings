from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile

from movies.models import Movie, MPAA_Rating, Genre


class TestModels(TestCase):

    def setUp(self):
        self.mpaa_rating = MPAA_Rating.objects.create(type="PG", label="Test Label")
        self.genre_1 = Genre.objects.create(name="Action")
        self.genre_2 = Genre.objects.create(name="Romantic")
        self.genre_3 = Genre.objects.create(name="Comedy")
        self.small_gif = (
            b"\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x00\x00\x00\x21\xf9\x04"
            b"\x01\x0a\x00\x01\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02"
            b"\x02\x4c\x01\x00\x3b"
        )
        self.movie_1 = Movie.objects.create(
            id=1,
            name="Test Movie",
            description="Test Description",
            mpaa_rating=self.mpaa_rating,
            image=SimpleUploadedFile(
                "small.gif", self.small_gif, content_type="image/gif"
            ),
        )
        self.movie_1.genres.add(self.genre_1)
        self.movie_1.genres.add(self.genre_2)
        self.movie_1.genres.add(self.genre_3)

    def test_movie_get_genre_list_string(self):
        expected = "Action, Romantic, Comedy"
        reality = self.movie_1.get_genres_string()
        self.assertEqual(expected, reality)
