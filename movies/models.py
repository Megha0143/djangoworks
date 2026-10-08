from django.db import models

# Create your models here.

class Movie(models.Model):
    movie_name=models.CharField(max_length=30)
    language=models.CharField(max_length=30)
    director=models.CharField(max_length=30)
    release_year=models.IntegerField()
    duration=models.IntegerField()
    rating=models.FloatField()

