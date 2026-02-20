from django.shortcuts import render
from .models import Game, Review

def games_list(request):
    games = Game.objects.all()
    return render(request, 'games/games_list.html', {'games': games})

def game_reviews(request, pk): #ISSUE: 1 zapytanie o listę recenzji + X zapytań o każdego autora z osobna  lepiej zrobic joina czylis select_related()
    reviews = Review.objects.filter(game_id = pk).select_related("author")
    return render(request, 'games/review_list.html', {'reviews': reviews})