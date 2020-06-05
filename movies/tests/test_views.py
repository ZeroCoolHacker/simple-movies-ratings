from django.test import TestCase, Client
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile

from movies.models import Movie, MPAA_Rating


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.list_url = reverse("movies:list")
        self.detail_url = reverse("movies:detail", args=[1])
        self.wrong_detail_url = reverse("movies:detail", args=[999999])
        self.mpaa_rating = MPAA_Rating.objects.create(type="PG", label="Test Label")
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
            image=SimpleUploadedFile("small.gif", self.small_gif, content_type="image/gif"),
        )

    def test_movies_list_GET(self):
        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "movies/home.html")

    def test_movie_detail_GET(self):
        response = self.client.get(self.detail_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "movies/detail.html")

    def test_movie_wrong_slug_404(self):
        response = self.client.get(self.wrong_detail_url)

        self.assertEqual(response.status_code, 404)
        self.assertTemplateNotUsed(response, "movies/detail.html")