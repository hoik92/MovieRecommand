from django.shortcuts import render, get_object_or_404
from movies.models import Genre, Movie, Score
from django.contrib.auth.models import User
from .serializers import GenreSerializer, ScoreSerializer, MovieSerializer, GenreDetailSerializer, UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

@api_view(['GET'])
def genre_list(request):
    genres = Genre.objects.all()
    serializer = GenreSerializer(genres, many=True)
    return Response(serializer.data)
    
@api_view(['GET'])
def genre_movie(request, genre_pk):
    genre = get_object_or_404(Genre, id=genre_pk)
    serializer = GenreDetailSerializer(genre)
    return Response(serializer.data)

@api_view(['GET'])
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)
    
@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, id=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)
    
@api_view(['GET', 'POST'])
def score_create(request, movie_pk):
    if request.method == 'POST':
        request.data['movie'] = movie_pk
        request.data['user'] = request.user.id
        request.data['username'] = request.user.username
        serializer = ScoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "작성되었습니다."
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        movie = get_object_or_404(Movie, id=movie_pk)
        scores = movie.scores.all()
        serializer = ScoreSerializer(scores, many=True)
        return Response(serializer.data)

@api_view(['PUT', 'DELETE'])
def score_edit(request, score_pk):
    score = get_object_or_404(Score, id=score_pk)
    request.data['movie'] = score.movie.id
    request.data['user'] = request.user.id
    request.data['username'] = request.user.username
    if request.method == 'PUT':
        serializer = ScoreSerializer(score, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "수정되었습니다."
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        # print(score)
        score.delete()
        return Response({
            "message": "삭제되었습니다."
        })
        

@api_view(['GET'])
def user_list(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def user_detail(request, user_id):
    user = get_object_or_404(User, id=user_id)
    serializer = UserSerializer(user)
    return Response(serializer.data)
    
@api_view(['GET'])
def login_user(request):
    user = request.user
    data = {
        "id": user.id,
        "username": user.username
    }
    return Response(data)