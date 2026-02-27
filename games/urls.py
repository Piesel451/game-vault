from django.urls import path
from . import views

urlpatterns = [
    path('', views.games_list, name='games_list'),
    path('review/<int:pk>/', views.game_reviews, name='game_reviews')
]