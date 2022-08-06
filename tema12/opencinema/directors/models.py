from pyexpat import model
from django.db import models

# Create your models here.

class Director(models.Model):
    directorId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=False)
    nationality = models.CharField(max_length=30)

    def __str__(self):
        txt = "{0}"
        return txt.format(self.name)

class Film(models.Model):
    filmId = models.CharField(max_length=3, primary_key=True)
    filmName = models.CharField(max_length=50, null=False)
    genres = [
        ('A', 'Action movies'),
        ('H', 'Horror'),
        ('D', 'Drama'),
        ('S', 'Sci-Fi'),
        ('N', 'Animation'),
        ('C', 'Comedy'),
        ('O', 'Documentary')
    ]
    genre = models.CharField(max_length=1, choices=genres)
    year = models.CharField(max_length=4)
    director = models.ForeignKey(Director, null=False, blank=False, on_delete=models.CASCADE)

    def movie(self):
        txt = "{0} {1} {2}"
        return txt.format(self.filmName, self.genre, self.year)

    def __str__(self):
        txt = "Film: {0} - {1} {2} (Director: {3})"
        return txt.format(self.filmName, self.genre, self.year, self.director)