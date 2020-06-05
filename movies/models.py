from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

MPAA_Ratings_CHOICES = [
    ('G', 'G'),
    ('PG', 'PG'),
    ('PG-13', 'PG-13'),
    ('R', 'R'),
    ('NC-17', 'NC-17'),
    ('M18', 'M18'),
    ('R21', 'R21'),
    ('M', 'M')
]
class Genre(models.Model):
    """Model Definition for Genre"""

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class MPAA_Rating(models.Model):
    """Model Definition for MPAA_Rating"""

    type = models.CharField(choices=MPAA_Ratings_CHOICES, max_length=5)
    label = models.TextField()

    def __str__(self):
        return f'{self.type} - {self.label}'

class Movie(models.Model):
    """Model definition for Movie."""

    name        = models.CharField(max_length=50, blank=False)
    description = models.TextField(blank=False)
    image       = models.ImageField(upload_to='images')
    duration    = models.IntegerField(default=1, validators=[MinValueValidator(1)])
    genres      = models.ManyToManyField(Genre)
    language    = models.CharField(max_length=50)
    mpaa_rating = models.ForeignKey(MPAA_Rating, on_delete=models.CASCADE)
    user_rating = models.IntegerField(default=1, validators=[MaxValueValidator(5), MinValueValidator(1)])
    class Meta:
        """Meta definition for Movie."""

        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'

    def __str__(self):
        """Unicode representation of Movie."""
        return self.name

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('movies:detail', kwargs={'pk': self.pk})
