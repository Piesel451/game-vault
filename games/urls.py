from django.urls import path
from . import views

app_name = "games"

urlpatterns = [
    path('', views.games_list, name='games_list'),
    path('review/<int:pk>/', views.game_reviews, name='game_reviews'),
    path('game/<int:pk>/', views.game_detail, name='game_detail')
]