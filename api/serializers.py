from rest_framework import serializers
from movies.models import Genre, Movie, Score
from django.conf import settings
from django.contrib.auth.models import User

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name', 'genreId',]
        
class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = ['id', 'content', 'score', 'movie', 'user', 'username',]

class MovieSerializer(serializers.ModelSerializer):
    scores = ScoreSerializer(many=True)
    genres = GenreSerializer(many=True)
    class Meta:
        model = Movie
        fields = ['id', 'title', 'audience', 'poster_url', 'description', 'genres', 'scores',]
        
class GenreDetailSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many=True)
    class Meta:
        model = Genre
        fields = ['id', 'movies', 'name',]
        
class UserSerializer(serializers.ModelSerializer):
    scores = ScoreSerializer(many=True)
    class Meta:
        model = User
        fields = ['username', 'is_superuser', 'scores',]