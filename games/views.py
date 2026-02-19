from django.shortcuts import render
from .models import Game, Review

def games_list(request):
    games = Game.objects.all()
    return render(request, 'games/games_list.html', {'games': games})

def game_reviews(request, pk): #ISSUE: 1 zapytanie o listę recenzji + X zapytań o każdego autora z osobna  lepiej zrobic joina czylis select_related()
    game = Game.objects.get(id = pk)
    reviews = game.game_reviews.all()
    return render(request, 'games/review_list.html', {'reviews': reviews})