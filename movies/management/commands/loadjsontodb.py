from django.core.management.base import BaseCommand
from django.utils import timezone
import json

class Command(BaseCommand):
    help = 'Loads the provided movie.json data into the database'

    def handle(self, *args, **kwargs):
        filename = 'demodata/movies.json'
        with open(filename) as f:
            data = json.load(f)
            for movie in data:
                print(f"id: {movie['id']}")
                print(f"name: {movie['name']}")
                print(f"description: {movie['description']}")
                print(f"imgPath: {movie['imgPath']}")
                print(f"duration: {movie['duration']}")
                for genre in movie['genre']:
                    print(f"genre: {genre}")
                print(f"language: {movie['language']}")
                print(f"mpaaRating-type: {movie['mpaaRating']['type']}")
                print(f"mpaaRating-label: {movie['mpaaRating']['label']}")
                print(f"userRating: {movie['userRating']}")
            print(f"Total Elements in this file were {len(data)}")
                