from django.core.management.base import BaseCommand
from django.utils import timezone
from django.core.files import File
import json
from movies.models import Movie, MPAA_Rating, Genre
import os

class Command(BaseCommand):
    help = 'Loads the provided movie.json data into the database'

    def handle(self, *args, **kwargs):
        filename = 'demodata/movies.json'
        with open(filename) as f:
            data = json.load(f)
            for movie in data:
                id           = movie['id']
                name         = movie['name']
                description  = movie['description']
                image        = File(open(os.path.join('demodata', movie['imgPath']), 'rb'))
                duration     = movie['duration']
                genre_list   = movie['genre']
                language     = movie['language']
                mpaa_rating  = movie['mpaaRating']
                user_rating  = movie['userRating']

                # Create MPAARating Object
                rating_obj = MPAA_Rating.objects.create(type=mpaa_rating['type'],label=mpaa_rating['label'])

                # Create Movie Object
                movie = Movie.objects.create(
                    pk=id,
                    name=name,
                    description=description,
                    image=image,
                    duration=duration,
                    language=language,
                    mpaa_rating=rating_obj,
                    user_rating=user_rating
                )
                # Add Genre Objects
                for genra in genre_list:
                    obj, created = Genre.objects.get_or_create(name=genra)
                    movie.genres.add(obj)

                try:
                    movie.save()
                except Exception as e:
                    print(f"Could not add object {movie} into database")
                    print(e)
            print(f"Total Elements in this file were {len(data)}")
