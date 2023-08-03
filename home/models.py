from django.db import models

# Create your models here.
class Movie(models.Model):
    movie_name = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    release_date = models.IntegerField()
    Genre = models.CharField(max_length=100)
    imdb = models.IntegerField()


class Test(models.Model):
    test_name = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    release_date = models.IntegerField()
    genre = models.CharField(max_length=100)
    imdb = models.IntegerField()
