from django.urls import path
from . import views
from rest_framework_swagger.views import get_swagger_view

app_name="api"

urlpatterns = [
    path('genres/', views.genre_list),
    path('genres/<int:genre_pk>/', views.genre_movie, name='genre_movie'),
    
    path('movies/', views.movie_list, name='movie_list'),
    path('movies/<int:movie_pk>/', views.movie_detail, name='movie_detail'),
    
    path('movies/<int:movie_pk>/scores/', views.score_create, name='score_create'),
    path('scores/<int:score_pk>/', views.score_edit, name='score_edit'),
    
    path('accounts/', views.user_list),
    path('accounts/<int:user_id>/', views.user_detail),
    path('accounts/login_user/', views.login_user),
    
    path('docs/', get_swagger_view(title='API')),
]