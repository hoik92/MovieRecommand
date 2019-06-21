from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('signup/', views.signup, name='signup'),
    
    path('admin/', views.user_admin, name='admin'),
    path('admin/<int:user_id>/', views.user_detail, name="user_detail"),
    path('admin/<int:user_id>/delete/', views.user_delete, name="user_delete"),
]