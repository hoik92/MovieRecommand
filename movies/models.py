from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=50)
    genreId = models.IntegerField()
    
class Movie(models.Model):
    title = models.CharField(max_length=100)
    audience = models.IntegerField()
    poster_url = models.CharField(max_length=200)
    description = models.TextField()
    # genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='movies')
    genres = models.ManyToManyField(Genre, related_name='movie', blank=True)
    
class Score(models.Model):
    content = models.CharField(max_length=100)
    score = models.IntegerField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='scores')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='scores')
    username = models.CharField(max_length=100)