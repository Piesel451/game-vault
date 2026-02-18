from django.urls import path
from . import views

urlpatterns = [
    path('', views.game_list, name='game_list'),
    path('review/<int:pk>', views.review, name='game_list')
]